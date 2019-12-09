import App.Model.Model as model
import App.View.View as view


def start():
    view.startView()
    input_key = input()
    model1 = model.Model();
    if input_key == 'y':
        print(model1.addNumbers())
        view.functionYes()
        return start()
    else:
        return view.endView()


if __name__ == "__main__":
    print('MVC - the simplest example')
    start()
