from django.db.models.signals import post_save
from django.dispatch import receiver
from django_q.tasks import async_task
from .models import Text

# Signals are blocking. They are not run in new threads or async or anything.
# So, must process them as quickly as a web-request.

@receiver(post_save, sender=Text)
def TextModel_save_callback(sender, instance, created: bool, raw: bool, using,
                            update_fields: set, **kwargs):
    if created:
        # New instance, need to process into phrases
        async_task('reader.tasks.new_phrases',
                   text_id=instance.pk)
    elif 'text' in update_fields:
        # If text is being updated, reprocess the phrases for this text
        async_task('reader.tasks.update_phrases',
                   text_id=instance.pk)
    # else text isn't being updated, so can ignore this.
    # note, if text instance is being deleted, post_save() signal isn't sent
    # but delete on cascade settings on model should remove phrases
