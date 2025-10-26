from django.shortcuts import render, redirect, get_object_or_404
from .models import Word
from .forms import WordForm
import random

# Create your views here.
def main(request):
    return render(request, 'main.html')

def add_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = WordForm()
    
    return render(request, 'add_word.html', {'form': form})

def delete_word(request):
    words = Word.objects.all().order_by('-id')
    return render(request, 'delete_word.html', {'words': words})

def learn_word(request):
    feedback = None

    if request.method == 'POST':
        word_id = request.POST.get('word_id')
        turkish_guess = request.POST.get('turkish_guess', '').strip().lower()

        try:
            questioned_word = Word.objects.get(id=word_id)
            correct_answer = questioned_word.turkish.strip().lower()

            if turkish_guess == correct_answer:
                feedback = {
                    'is_correct': True,
                    'message': f"Doğru! ({questioned_word.english} - {questioned_word.turkish})"
                }
            else:
                feedback = {
                    'is_correct': False,
                    'message': f"Yanlış. {questioned_word.english} - {questioned_word.turkish}"
                }
        except Word.DoesNotExist:
            feedback = {
                'is_correct': False, 
                'message': 'Bir hata oluştu. Kelime bulunamadı.'
            }
    word_to_ask = None
    all_words = list(Word.objects.all())

    if all_words:
        word_to_ask = random.choice(all_words)
    
    return render(request, 'learn_word.html', {
        'word': word_to_ask,
        'feedback': feedback,
    })

def delete_word_action(request, word_id):
    word_to_delete = get_object_or_404(Word, id=word_id)
    if request.method == 'POST':
        word_to_delete.delete()
    return redirect('delete-word')