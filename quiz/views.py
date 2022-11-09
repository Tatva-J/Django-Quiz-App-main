from django.shortcuts import render, redirect
from .models import Question
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def index_page(request):
    return render(request, "index.html")


# questions = Question.objects.filter(level=request.POST.get("level")).order_by("?")[
#         : int(request.POST.get("max")) + 1
#     ]


@login_required(login_url="/login/")
def before_quiz(request):
    questions = Question.objects.filter(level=request.POST.get("level")).order_by("?")[
        : int(request.POST.get("max"))
    ]
    paginator = Paginator(questions, 1)
    page_number = request.GET.get("page")
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        "questions": questions,
        "page_obj": page_obj,
        "level": request.POST.get("level"),
        "max": request.POST.get("max"),
    }

    if request.method == "GET":
        request.session["previous_page"] = (
            request.path_info + "?page=" + request.GET.get("page", "1")
        )
        # request.query_params._mutable = True

        return render(request, "quiz.html", context)
    if request.method == "POST" and not request.POST.get("level"):
        correct_user_answers = []
        user_answer = request.POST["option"]
        correct_answer = request.POST.get("answerLabel")
        print("correct answer ", correct_answer)
        print("user answer: ", user_answer)
        if user_answer == correct_answer:
            correct_user_answers.append(user_answer)
            messages.success(request, "Correct answer")
            return HttpResponseRedirect(request.session["previous_page"])
        else:
            messages.warning(
                request, f"Wrong answer, Correct Answer is {correct_answer}"
            )
            return HttpResponseRedirect(request.session["previous_page"])
    if request.method == "POST":
        request.session["previous_page"] = (
            request.path_info + "?page=" + request.GET.get("page", "1")
        )
        # request.GET._mutable = True
        # request.GET["max"] = request.POST.get("max")
        # request.GET["level"] = request.POST.get("level")
        return render(request, "quiz.html", context)


@login_required(login_url="/login/")
def take_quiz(request):
    #!Task1=Randomly picking max number of questions=finished
    # questions = Question.objects.filter(level="Easy")
    questions = Question.objects.filter(level=request.GET.get("level")).order_by("?")[
        : int(request.GET.get("max"))
    ]
    paginator = Paginator(questions, 1)
    page_number = request.GET.get("page")
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        "questions": questions,
        "page_obj": page_obj,
        "level": request.GET.get("level"),
        "max": request.GET.get("max"),
    }

    if request.method == "GET":
        request.session["previous_page"] = (
            request.path_info + "?page=" + request.GET.get("page", "1")
        )
        # request.query_params._mutable = True

        return render(request, "quiz.html", context)
    if request.method == "POST" and not request.POST.get("level"):
        correct_user_answers = []
        user_answer = request.POST["option"]
        correct_answer = request.POST.get("answerLabel")
        print("correct answer ", correct_answer)
        print("user answer: ", user_answer)
        if user_answer == correct_answer:
            correct_user_answers.append(user_answer)
            messages.success(request, "Correct answer")
            return HttpResponseRedirect(request.session["previous_page"])
        else:
            messages.warning(
                request, f"Wrong answer, Correct Answer is {correct_answer}"
            )
            return HttpResponseRedirect(request.session["previous_page"])
    if request.method == "POST":
        request.session["previous_page"] = (
            request.path_info + "?page=" + request.GET.get("page", "1")
        )
        # request.GET._mutable = True
        # request.GET["max"] = request.POST.get("max")
        # request.GET["level"] = request.POST.get("level")
        return render(request, "quiz.html", context)
