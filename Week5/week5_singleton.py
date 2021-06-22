class SingletonExec:
   __instance__ = None

   def __init__(self):
       if SingletonExec.__instance__ is None:
           SingletonExec.__instance__ = self
       else:
           raise Exception("You cannot create another SingletonExec class")

   @staticmethod
   def get_instance():
       if not SingletonExec.__instance__:
           SingletonExec()
       return SingletonExec.__instance__

if __name__ == "__main__":
    organization = SingletonExec()
    print(organization)

    same_organization = SingletonExec.get_instance()
    print(same_organization)

    another_organization = SingletonExec.get_instance()
    print(another_organization)

    new_organization = SingletonExec()
    print(new_organization)
