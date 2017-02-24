from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from django.contrib.auth import get_user_model
from django.db import IntegrityError
from .models import Choice, Question, UserAnswer, User



class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions (not including
		those to be published in the future).
		"""
		return Question.objects.filter(
			pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'
	def get_quesryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = UserAnswer
	template_name = 'polls/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
		UserAnswer.objects.create(user = request.user, 
			                      question=question, choice=selected_choice)
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
			})
	except IntegrityError as e:
			return render(request, 'polls/detail.html', {
				'question': question,
				'error_message': "Вы уже голосовали",
				})
	else:
		selected_choice.votes += 1
		selected_choice.save()

	return render(request, 'polls/results.html', {'question': question})

def users(request):
	User = get_user_model()
	users = User.objects.all()
	return render(request, 'polls/list_users.html', {'users': users})

def answer(request, user_id):
	user_answers = UserAnswer.objects.filter(user_id=user_id)
	return render(request, 'polls/list_answer.html', 
					{'user_answers': user_answers, })