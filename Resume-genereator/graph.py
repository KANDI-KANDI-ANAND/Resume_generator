from langgraph.graph import StateGraph, START, END
from schemas import ResumeClass


from nodes import (
    Resume_Parser_node,
    Skill_Extractor_node,
    JD_Analyser_node,
    skill_matcher_node,
    gap_analyser_node,
    planner_node,
    rewriter_node,
    ats_validator_node,
    PDF_builder_node
)

from router import route_evaluation

graph = StateGraph(ResumeClass)


graph.add_node('resume_parser', Resume_Parser_node)
graph.add_node('skill_extractor', Skill_Extractor_node)
graph.add_node('jd_analyser', JD_Analyser_node)
graph.add_node('skill_matcher', skill_matcher_node)
graph.add_node('gap_analyser', gap_analyser_node)
graph.add_node('planner', planner_node)
graph.add_node('writer', rewriter_node)
graph.add_node('ats_validator', ats_validator_node)
graph.add_node('pdf_builder', PDF_builder_node)


graph.add_edge(START, 'resume_parser')
graph.add_edge('resume_parser', 'skill_extractor')
graph.add_edge('skill_extractor', 'jd_analyser')
graph.add_edge('jd_analyser', 'skill_matcher')
graph.add_edge('skill_matcher', 'gap_analyser')
graph.add_edge('gap_analyser', 'planner')
graph.add_edge('planner', 'writer')
graph.add_edge('writer', 'ats_validator')
graph.add_conditional_edges('ats_validator', route_evaluation,{
    'approved': 'pdf_builder',
    'needs_improvement': 'planner'
})
graph.add_edge('pdf_builder', END)


workflow = graph.compile()