from prefect import flow, task


@task
def say_hello():
    print("Hello World!")


@flow(name="Hello Flow")
def hello_flow():
    say_hello()


if __name__ == "__main__":
    # Déployer le flow avec la nouvelle syntaxe
    hello_flow.serve(
        name="hello-deployment",
        version="1",
        work_queue='default'
    )
