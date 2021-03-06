from celery import Celery
import subprocess

app = Celery('tasks', backend='amqp', broker='pyamqp://user:password@192.168.1.12:5672/vhost')

@app.task
def airfoil_simulation(angle, n_nodes, n_levels, num_samples, viscosity, velocity, duration):
    subprocess.run(["./airfoil_task.sh", angle, n_nodes, n_levels, num_samples, viscosity, velocity, duration])
    # Use subprocess.Popen(["some script"]) so that we can use Popen.wait to ask python to wait for the subprocess to complete before it runs another one from the queue
    #results = subprocess.run(['docker', 'exec', '-it', 'airfoil', 'cat', 'results/drag_ligt.m'], stdout=subprocess.PIPE)
    #print(results.stdout)
    return ("done")
