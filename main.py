import bussines_model.Worker as worker
import bussines_model.Process as proc
import bussines_model.Factory as factory

if __name__ == '__main__':
    p = proc.Process()
    w1 = worker.Worker("w1", "1", p.jobs["P"])
    w2 = worker.Worker("w2", "2", p.jobs["AS"])

    p.new_proc("D", "Deliver")
    w3 = worker.Worker("w3", "3", p.jobs["D"])
    wl = [w1,w2,w3]
    factory = factory.Factory(wl)
    factory.start_shift(wl, p)

