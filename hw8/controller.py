import view
import model

def start():

    example = view.input_exaple()
    example = model.transformations(example)
    view.show_example(example)
    old_example = example.copy()
    
    while len(example) > 1:
        model.calculate(example, '*', '/')
        model.calculate(example, '+', '-')

    view.show_result(example, old_example)