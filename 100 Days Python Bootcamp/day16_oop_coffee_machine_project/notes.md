Attributes are the fancy variables for the classes.

Methods are the specific functions that class do.

Exp:
    Restaurant Simulation
        
    Waiter class has is_holding_plate = True --> This is an attribute, unique to this class.
    Waither class has 
        def take_order(table,order):
            #takes order to chef
        This is a method.
Attributes are answer the question "What they have?".

On the other hand methods answers the question "What they do?"

An object can be crated from class one class can have multiple objects. Like in a restaurant you can have more than one waiter but in the core of things they do the same job with little difference like they can tend different tables.

    car = CarBlueprint()
    object_name = ClassName() #This is the way we are going to name our classes and objects.For readibility and clean code purposes.

Turtle Library

    # import turtle          | This a one way to import things.
    # aina = turtle.Turtle() |
    from turtle import Turtle,Screen # This is another way.

    aina = Turtle()
    print(aina)
    aina.shape("turtle")
    aina.color("DarkSlateGray","azure")
    aina.forward(100)

    my_screen = Screen()
    print(my_screen.canvheight)
    my_screen.exitonclick() #It is a method that allows us to use the screen until we decide the click screen.

Learning to use PrettyTable

    from prettytable import PrettyTable
    
    table = PrettyTable()
    
    table.add_column("Pokemon Name",["Pikachu","Squirtle","Gulpin"],"r")
    table.add_column("Pokemon Type",["Electricity","Water","Poison"],"r")
    print(table)