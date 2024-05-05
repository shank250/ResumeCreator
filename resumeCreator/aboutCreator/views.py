
from django.shortcuts import render
from .form import UserInputForm
from .ResumeAboutCreatorATS import aboutReturn
def user_input_view(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            result = aboutReturn(user_input)
            # result = process_user_input(user_input)
            return render(request, 'result.html', {'result': result})
    else:
        form = UserInputForm()
    return render(request, 'input.html', {'form': form})

def process_user_input(user_input):
    result = aboutReturn(user_input)
    # result = process_user_input(user_input)
    return result