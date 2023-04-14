function checkAnswer(correct_answer, answer_id, el){
    if (answer_id === correct_answer)
    {
        el.classList.add("correct");
    }
    else 
    {
        el.classList.add("wrong");
    }
}