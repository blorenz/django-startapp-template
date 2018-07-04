import graphene



class ExampleMutation(graphene.Mutation):
    class Arguments:
        hello = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, info, tribe_name, password):
            return ExampleMutation(ok=True)


class AllMutations(object):
    example_mutation = ExampleMutation.Field()
