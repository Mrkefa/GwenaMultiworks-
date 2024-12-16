import json
import openai
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from myapp.forms import ImageUploadForm
from myapp.models import Message, ImageModel
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Booking
from django.contrib.auth import logout





# Create your views here.
def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def blogs(request):
    return render(request,'blog-details.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    if request.method=='POST':
        mymessage=Message(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            message=request.POST['message'],
        )
        mymessage.save()
        return redirect('/')
    else:
        return render(request, 'index.html')

def service(request):
    return render(request,'service-details.html')

def project(request):
    return render(request,'project-details.html')

def hire(request):
    return render(request,'hire.html')

def projects(request):
    return render(request,'projects.html')

def services(request):
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get("name")
        address = request.POST.get("address")
        location = request.POST.get("location")
        company_name = request.POST.get("company_name")
        contact_info = request.POST.get("contact_info")
        service_date = request.POST.get("service_date")
        service_type = request.POST.get("service_type")
        budget = request.POST.get("budget")

        # Save the form data into the database
        Booking.objects.create(
            name=name,
            address=address,
            location=location,
            company_name=company_name,
            contact_info=contact_info,
            service_date=service_date,
            service_type=service_type,
            budget=budget
        )

        # Pass a success message back to the template
        success_message = "Your order has been successfully submitted!"
        return render(request, "assets.html", {"success_message": success_message})

    else:
        # Render the form for GET requests
        return render(request, "services.html")

def starter(request):
    return render(request,'starter-page.html')

def order(request):
    return render(request,'order.html')



from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Booking


def assets(request):
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get("name")
        address = request.POST.get("address")
        location = request.POST.get("location")
        company_name = request.POST.get("company_name")
        contact_info = request.POST.get("contact_info")
        service_date = request.POST.get("service_date")
        service_type = request.POST.get("service_type")
        budget = request.POST.get("budget")

        # Save form data into the database associated with the logged-in user
        Booking.objects.create(
            user=request.user,  # Associate booking with the logged-in user
            name=name,
            address=address,
            location=location,
            company_name=company_name,
            contact_info=contact_info,
            service_date=service_date,
            service_type=service_type,
            budget=budget
        )

        # Pass a success message back to the template
        success_message = "Your order has been successfully submitted!"
        return render(request, "assets.html", {"success_message": success_message})

    else:
        # Render the form for GET requests
        return render(request, "assets.html")




def roads(request):
    return render(request,'roads.html')

def blog1(request):
    return render(request,'blog1.html')

def blog2(request):
    return render(request,'blog2.html')

def blog3(request):
    return render(request,'blog3.html')

def asset2(request):
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get("name")
        address = request.POST.get("address")
        location = request.POST.get("location")
        company_name = request.POST.get("company_name")
        contact_info = request.POST.get("contact_info")
        service_date = request.POST.get("service_date")
        service_type = request.POST.get("service_type")
        budget = request.POST.get("budget")

        # Save the form data into the database
        Booking.objects.create(
            name=name,
            address=address,
            location=location,
            company_name=company_name,
            contact_info=contact_info,
            service_date=service_date,
            service_type=service_type,
            budget=budget
        )

        # Pass a success message back to the template
        success_message = "Your order has been successfully submitted!"
        return render(request, "assets.html", {"success_message": success_message})

    else:
        # Render the form for GET requests
        return render(request, "asset2.html")


def asset3(request):
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get("name")
        address = request.POST.get("address")
        location = request.POST.get("location")
        company_name = request.POST.get("company_name")
        contact_info = request.POST.get("contact_info")
        service_date = request.POST.get("service_date")
        service_type = request.POST.get("service_type")
        budget = request.POST.get("budget")

        # Save the form data into the database
        Booking.objects.create(
            name=name,
            address=address,
            location=location,
            company_name=company_name,
            contact_info=contact_info,
            service_date=service_date,
            service_type=service_type,
            budget=budget
        )

        # Pass a success message back to the template
        success_message = "Your order has been successfully submitted!"
        return render(request, "assets.html", {"success_message": success_message})

    else:
        # Render the form for GET requests
        return render(request, "asset3.html")


def asset4(request):
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get("name")
        address = request.POST.get("address")
        location = request.POST.get("location")
        company_name = request.POST.get("company_name")
        contact_info = request.POST.get("contact_info")
        service_date = request.POST.get("service_date")
        service_type = request.POST.get("service_type")
        budget = request.POST.get("budget")

        # Save the form data into the database
        Booking.objects.create(
            name=name,
            address=address,
            location=location,
            company_name=company_name,
            contact_info=contact_info,
            service_date=service_date,
            service_type=service_type,
            budget=budget
        )

        # Pass a success message back to the template
        success_message = "Your order has been successfully submitted!"
        return render(request, "assets.html", {"success_message": success_message})

    else:
        # Render the form for GET requests
        return render(request, "asset4.html")



from django.shortcuts import render, redirect
from .models import Booking

@login_required
def hire(request):
    """
    Handles the Hire form submission.
    """
    success_message = None  # Initialize success message as None (no message by default)

    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get("name")
        address = request.POST.get("address")
        location = request.POST.get("location")
        company_name = request.POST.get("company_name")
        contact_info = request.POST.get("contact_info")
        service_date = request.POST.get("service_date")
        service_type = request.POST.get("service_type")
        budget = request.POST.get("budget")

        # Save the booking to the database
        Booking.objects.create(
            user=request.user,  # Associate the booking with the logged-in user
            name=name,
            address=address,
            location=location,
            company_name=company_name,
            contact_info=contact_info,
            service_date=service_date,
            service_type=service_type,
            budget=budget
        )

        # Set the success message
        success_message = "Your order has been successfully submitted!"

    # Render the hire page with the success message (if any)
    return render(request, "hire.html", {"success_message": success_message})




def terms(request):
    return render(request,'terms.html')

def construction(request):
    return render(request,'construction.html')



def ai(request):
    return render(request, 'ai.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')

# Chatbot view
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def chatbot(request):
    """
    Endpoint for the chatbot. Matches user messages to predefined intents and responses.
    """
    if request.method == "POST":
        try:
            # Parse JSON payload from the request
            data = json.loads(request.body)
            user_message = data.get("message", "").lower().strip()

            if not user_message:
                return JsonResponse({"response": "Please provide a message to process."})

            # Define intent-response mapping
            responses = {
                "Hello": "Hi there! Welcome to our construction company. How can I assist you?",
                "hello": "Hi there! Welcome to our construction company. How can I assist you?",
                "hi": "Hello! How can I help you with your construction needs today?",
                "help": "Sure! What do you need help with? For example, services, pricing, or projects?",
                "who are you": "I’m your friendly assistant for our construction company, here to provide information about our services and projects.",
                "bye": "Goodbye! Feel free to reach out anytime. Have a great day!",

                # Construction-specific responses
                "what services do you offer": "We offer services such as residential and commercial construction, renovations, and project management.",
                "what are your services": "Our services include construction planning, design, building, site management, and interior design. What do you need help with?",
                "do you do renovations": "Yes, we specialize in renovations for homes and businesses. Let us know what project you have in mind!",
                "can you build a house": "Absolutely! We provide end-to-end construction services for custom homes and residential buildings.",
                "do you build commercial spaces": "Yes, we specialize in commercial construction, including offices, retail spaces, and warehouses.",

                # Pricing and quotes
                "how much do you charge": "Our pricing depends on the specifics of your project. Would you like us to provide a free quote?",
                "can i get a free quote": "Of course! Please provide details about your project, and we'll prepare a free quote for you.",
                "what is your pricing structure": "Our pricing is based on project size, materials, and timelines. We can discuss this further during a consultation.",

                # About the company
                "where are you located": "We are located at [Siaya County- Bondo town]. Let us know if you'd like to visit us!",
                "what is your location": "Our location is [Your Office Address]. We can also schedule a meeting at your convenience.",
                "how long have you been in business": "We have been in the construction business for over [10 years]. Our experience ensures quality and reliability.",
                "what makes you different": "Our commitment to quality, customer satisfaction, and innovative designs sets us apart in the construction industry.",

                # Miscellaneous
                "contact": "You can contact us via email at [cepomondi@gmail.com] or call us at [+254742003190].",
                "what are your working hours": "We are available Monday to Friday, 9 AM to 6 PM. Let us know how we can assist you.",
                "do you offer warranties": "Yes, we offer warranties on our construction work. Please ask us about specific details for your project.",
                "what is your process": "Our process includes consultation, planning, design, budgeting, and execution to ensure your project is seamless.",

                # Default response for unmatched queries
                "default": "I'm sorry, I don't understand. Can you rephrase your question or ask about our services, pricing, or company?"
            }

            # Match user input to predefined intents or provide a default response
            response = responses.get(user_message, "I'm sorry, I don't understand. type 'contact' to get help?")

            # Respond with the matched response or default fallback
            return JsonResponse({"response": response})

        except json.JSONDecodeError:
            # Handle invalid JSON
            return JsonResponse({"response": "Invalid JSON payload. Please send a valid JSON object."})
        except Exception as e:
            # Handle unexpected errors
            return JsonResponse({"response": f"An unexpected error occurred: {str(e)}"})

    # If the request method is not POST, return an error
    return render(request, 'chatbot.html')


@login_required
def my_account(request):
    """
    Display the list of orders made by the logged-in user.
    """
    if not request.user.is_authenticated:
        return redirect("login")  # Redirect to login if the user is not authenticated

    bookings = Booking.objects.filter(user=request.user)  # Fetch bookings for the logged-in user
    return render(request, "my_account.html", {"account": my_account, "bookings": bookings})


@login_required
def edit_booking(request, booking_id):
    # Fetch the booking object
    booking = Booking.objects.get(id=booking_id, user=request.user)

    if request.method == "POST":
        # Update booking details
        booking.name = request.POST.get("name")
        booking.address = request.POST.get("address")
        booking.location = request.POST.get("location")
        booking.company_name = request.POST.get("company_name")
        booking.contact_info = request.POST.get("contact_info")
        booking.service_date = request.POST.get("service_date")
        booking.service_type = request.POST.get("service_type")
        booking.budget = request.POST.get("budget")
        booking.save()

        return redirect("my_account")

    return render(request, "edit_booking.html", {"booking": booking})

@login_required
def cancel_booking(request, booking_id):
    # Fetch and delete booking
    booking = Booking.objects.get(id=booking_id, user=request.user)
    booking.delete()
    return redirect("my_account")



def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect("register")

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect("login")  # Redirect to login after successful registration

    return render(request, "register.html")






def signup(request):
    """
    Handles user signup and account creation.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()  # Create a new user
            login(request, user)  # Log the user in immediately
            return redirect("assets")  # Redirect to the order form page

    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})


def logout_view(request):
    logout(request)  # Log the user out
    return redirect("assets")  # Redirect to the assets page or login page

from flask import Flask, request, jsonify
import openai  # Replace this with HuggingFace if needed

app = Flask(__name__)

# OpenAI API Key for ChatGPT
openai.api_key = "YOUR_API_KEY"  # Replace with your OpenAI API Key



