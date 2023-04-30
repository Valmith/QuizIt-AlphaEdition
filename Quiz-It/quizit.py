import pgzrun

WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)

answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)

answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0

time_left = 15

q1 = ["Who is the murderer of europe during ww2?",
      "Charles Babbage", "Henry Ford", "Nikola Tesla", "Adolf Hitler", 4]



questions = [q1]

question = questions.pop(0)




game_state = "start"  # initial game state

def draw():
    screen.clear()
    
    if game_state == "start":
        # draw start screen
        screen.draw.text("Welcome to the Quiz Game!", (400, 200), color="white", fontsize=60)
        screen.draw.text("Click anywhere to start", (400, 400), color="white", fontsize=40)
    else:
        # draw game screen
        screen.fill("dim gray")
        screen.draw.filled_rect(main_box, "sky blue")
        screen.draw.filled_rect(timer_box, "sky blue")

        for box in answer_boxes:
            screen.draw.filled_rect(box, "Orange")

        screen.draw.textbox(str(time_left), timer_box, color=("black"))
        screen.draw.textbox(question[0], main_box, color=("black"))

        index = 1
        for box in answer_boxes:
            screen.draw.textbox(question[index], box, color=("black"))
            index = index + 1
        
    pass

def game_over():
    global question, time_left
    message = "Game over, You got %s questions correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0
    pass


def correct_answer():
    global question, score, time_left

    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 15

    else:
        print("End of questions")
        game_over()
    pass


def on_mouse_down(pos):

    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer" + str(index))
            if index == question[5]:
                print("Correct Answer!")
                correct_answer()
            else:
                game_over()
                
        index = index + 1
            
    global game_state
    if game_state == "start":
        game_state = "playing"
    else:
        # handle mouse click in game screen
        pass

def update_time_left():
    
    global time_left
    if time_left:
        time_left = time_left - 1
    else:
        game_over()
clock.schedule_interval(update_time_left, 1.0)
pass

pgzrun.go()
