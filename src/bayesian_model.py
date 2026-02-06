from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def create_bayesian_model():
    model = DiscreteBayesianNetwork([
        ('Rain', 'Traffic'),
        ('Traffic', 'Blockage')
    ])
    cpd_rain = TabularCPD(
        variable='Rain',
        variable_card=2,
        values=[[0.7], [0.3]]  # no rain, rain
    )

    cpd_traffic = TabularCPD(
        variable='Traffic',
        variable_card=2,
        values=[
            [0.8, 0.3],  # low traffic
            [0.2, 0.7]   # high traffic
        ],
        evidence=['Rain'],
        evidence_card=[2]
    )

    cpd_blockage = TabularCPD(
        variable='Blockage',
        variable_card=2,
        values=[
            [0.9, 0.4],  # no blockage
            [0.1, 0.6]   # blockage
        ],
        evidence=['Traffic'],
        evidence_card=[2]
    )
    model.add_cpds(cpd_rain, cpd_traffic, cpd_blockage)
    model.check_model()

    return model

def estimate_blockage_probability(rain):
    model = create_bayesian_model()
    inference = VariableElimination(model)

    result = inference.query(
        variables=['Blockage'],
        evidence={'Rain': rain}
    )

    return result.values[1]  # Probability of blockage = True
