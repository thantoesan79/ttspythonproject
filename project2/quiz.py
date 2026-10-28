import time;

def show_countdown(seconds):
    print(f"\n You have{seconds} seconds to answer !");
    #range(start,end,increase/decrease);
    for i in range(seconds, 0, -1):
        print(i, end=" ", flush=True)
        time.sleep(1)
    print("\n")

def ask_question(question,options,correct_answer,time_limit=10):
    #Ask a single question (mitliplec choice)
    #answer the question on time count 1 and otherwise 0;
    print(question);
    for option in  options:
        print(option);
    start_time = time.time();#current time
    answer = input("Enter the letter of your answer:").strip().upper();
    elapsed = time.time() - start_time;
    if elapsed > time_limit:
        print("Time Up!");
        return 0;
    elif answer == correct_answer:
         print("Correct Answer!\n")
         return 1
    else:
        print(f"Wrong answer ,The correct answer is {correct_answer} .\n")
        return 0
    
     
def main():
    """ 
     The Quiz game
       """
     
    print("Welcome  to the Timed Quiz Game!");
    score =0;
    time_limit = 10;
    question = [
        {
                "question": "What data type is used for True/False in Python ?",
                "option": ["A.str","B.bool","C.int","D.Char"],
                "answer": "B",
        },
        {
            "question": "What temple is the largest in Myanmar ?",
              "option":["A.Shwedagon","B.Ananda","C.Sulamani","D.Dhamayangyi"],
               "answer": "D",
        }
    ]

    for q in question:
        show_countdown(time_limit);
        score += ask_question(q["question"],q["option"],q["answer"]);
        print(f"Quiz is finished and your scores : {score} out of {len(question)}");


if   __name__ == "__main__":
    main();
 

      