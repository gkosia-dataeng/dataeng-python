'''
      Single Leading Underscore: _var
            Does not affect the behaivior of interptiter
            Shows to programmer that the variable/method is for internal use (hint private)
            Interptiter does not know about private/public access

      Single Trailing Underscore: var_
            Used to bypass naming conflict
            Cannot have two classes with name foo
            I can have one foo and one foo_

      Double Leading Underscore: __var

            "name mangling": interpriter adds the _ClassName in front of the class to prevend override the method/attribute from subclass
            To call/use the method/attribute have to refer as _ClassName__foo
      
      Double Leading and Trailing Underscore: __var__
            Magic methods
            Callable methods in object lifecycle evetns

      
      Single Underscore: _

            Placeholder or temporary or insignificant variable that will not used
            for _ in range(32):
                print("Hello")
'''

