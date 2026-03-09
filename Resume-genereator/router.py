from schemas import ResumeClass

def route_evaluation(state: ResumeClass):

    if state['Validation'] == 'approved' or state['iteration'] >= state['max_iteration']:
        return 'approved'
    else:
        return 'needs_improvement'