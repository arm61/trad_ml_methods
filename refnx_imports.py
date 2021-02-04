from refnx.dataset import ReflectDataset
from refnx.analysis import Objective
from refnx.reflect import SLD, ReflectModel


air = SLD(0.0, name='air')
tails = SLD(7.5, name='tail')
lipid = SLD(7.2, name='lipid')
heads = SLD(3.6, name='head')
d2o = SLD(0, name='d2o')


    
def one_layer(data):
    th_layer = lipid(22, 3.)
    w_layer = d2o(0, 3.)
    structure = air | th_layer | w_layer
    model = ReflectModel(structure, bkg=5e-6, dq=5.)
    model.bkg.setp(5e-6, vary=True, bounds=(1e-8, 1e-3))
    model.structure[1].thick.setp(20, vary=True, bounds=(22, 35))    
    return Objective(model, data)


def two_layer(data):
    t_layer = tails(18, 3.)
    h_layer = heads(10, 3.)
    w_layer = d2o(0, 3.)
    structure = air | t_layer | h_layer | w_layer
    model = ReflectModel(structure, bkg=5e-6, dq=5.)
    model.bkg.setp(5e-6, vary=True, bounds=(1e-8, 1e-3))
    model.structure[1].thick.setp(18, vary=True, bounds=(15, 25))
    model.structure[2].thick.setp(10, vary=True, bounds=(7, 12))
    return Objective(model, data)
