from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail



def about_view(request):
    return render(request, 'pages/about.html')


def contact_view(request):

    #if user click send email button
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            #get the data
            name = form.cleaned_data['name']
            email_from = form.cleaned_data['email']
            message = form.cleaned_data['message']

            #send_mail('The Subject', 'The Message', 'from@mail.com', ['to@email.com'])
            send_mail("Message from " + name, message, email_from, ['mariafeernanda.murillo@gmail.com']) 

            return redirect('about')

        else:
            print("The message can not be send")
            
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})
