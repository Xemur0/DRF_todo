import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from users.models import User
from project.models import Project, Todo


# LEVEL 1

# class Query(ObjectType):
#     hello = graphene.String(default_value="Hi")
#
# schema = graphene.Schema(query=Query)

# LEVEL 2

# class UserType(DjangoObjectType):
#
#     class Meta:
#         model = User
#         fields = '__all__'
#
# class Query(ObjectType):
#
#     all_users = graphene.List(UserType)
#
#     def resolve_all_users(root, info):
#         return User.objects.all()
#
# schema = graphene.Schema(query=Query)

# LEVEL 3

# class UserType(DjangoObjectType):
#
#     class Meta:
#         model = User
#         fields = '__all__'
#
# class ProjectType(DjangoObjectType):
#     class Meta:
#         model = Project
#         fields = '__all__'
#
# class Query(ObjectType):
#
#     all_users = graphene.List(UserType)
#     all_projects = graphene.List(ProjectType)
#
#     def resolve_all_users(root, info):
#         return User.objects.all()
#
#     def resolve_all_projects(root, info):
#         return Project.objects.all()
#
#
# schema = graphene.Schema(query=Query)

# LEVEL 4

# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = '__all__'
#
#
# class ProjectType(DjangoObjectType):
#     class Meta:
#         model = Project
#         fields = '__all__'
#
#
# class Query(ObjectType):
#     project_by_id = graphene.Field(ProjectType, id=graphene.Int(required=True))
#
#     def resolve_project_by_id(root, info, id=None):
#         if id:
#             return Project.objects.get(id=id)
#         return None
#
#     project_by_name = graphene.List(ProjectType, name=graphene.String(required=False))
#
#     def resolve_project_by_name(root, info, name=None):
#
#         projects = Project.objects.all()
#
#         if name:
#             return projects.filter(name=name)
#         return projects
#
#
# schema = graphene.Schema(query=Query)


# LEVEL 5

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class Query(ObjectType):
    project_by_id = graphene.Field(ProjectType, id=graphene.Int(required=True))

    def resolve_project_by_id(root, info, id=None):
        if id:
            return Project.objects.get(id=id)
        return None

    project_by_name = graphene.List(ProjectType, name=graphene.String(required=False))

    def resolve_project_by_name(root, info, name=None):

        projects = Project.objects.all()

        if name:
            return projects.filter(name=name)
        return projects

    todo_by_project = graphene.List(TodoType, name=graphene.String(required=False))

    def resolve_todo_by_project(root, info, name=None):
        todo = Todo.objects.all()
        if name:
            return todo.filter(project__name=name)
        return todo


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(root, info, username, id):
        user = User.objects.get(id=id)
        user.username = username
        user.save()
        return UserUpdateMutation(user=user)


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        first_name = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(root, info, username, first_name, email):
        user = User.objects.create(username=username, first_name=first_name, email=email)
        return UserCreateMutation(user=user)


class UserDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    user = graphene.List(UserType)

    @classmethod
    def mutate(root, info, id):
        User.objects.get(id=id).delete()
        user = User.objects.all()
        return UserCreateMutation(user=user)

class TodoUpdateMutation(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=False)
        id = graphene.ID()

    todo = graphene.Field(TodoType)

    @classmethod
    def mutate(root, info, text, id):
        todo = Todo.objects.get(id=id)
        todo.text = text
        todo.save()
        return TodoUpdateMutation(todo=todo)

class TodoCreateMutation(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=False)
        is_active = graphene.Boolean(required=False)
        creator = graphene.Int(required=True)
        project = graphene.Int(required=True)

    todo = graphene.Field(TodoType)

    @classmethod
    def mutate(root, info, text, is_active, creator=None, project=None):
        project = Project.objects.get(id=project)
        creator = User.objects.get(id=creator)
        todo = Todo.objects.create(text=text, is_active=is_active, creator=creator, project=project)
        return TodoCreateMutation(todo=todo)

class TodoDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    todo = graphene.List(TodoType)

    @classmethod
    def mutate(root, info, id):
        Todo.objects.get(id=id).delete()
        todo=Todo.objects.all()
        return TodoCreateMutation(todo=todo)


class Mutation(graphene.ObjectType):
    update_user = UserUpdateMutation.Field()
    create_user = UserCreateMutation.Field()
    delete_user = UserDeleteMutation.Field()
    update_todo = TodoUpdateMutation.Field()
    create_todo = TodoCreateMutation.Field()
    delete_todo = TodoDeleteMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
