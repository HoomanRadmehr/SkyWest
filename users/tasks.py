import celery
from verify_email.email_handler import send_verification_email

@celery.shared_task(name="send verifiction email")
def send_verifiction_emai_task(request, form):
    send_verification_email(request,form)
    