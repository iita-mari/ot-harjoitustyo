from invoke import task

@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def start_invoke(ctx)
    ctx.run("poetry run invoke test")

@task
def test_invoke(ctx):
    ctx.run("poetry run invoke test")

@task
def coverage_invoke(ctx):
    ctx.run("poetry run invoke coverage-report")

@task(coverage_invoke)
def coverage_invoke_report(ctx):
    ctx.run("coverage html", pty=True)

