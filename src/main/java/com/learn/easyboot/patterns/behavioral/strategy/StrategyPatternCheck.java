//package com.learn.easyboot.patterns.behavioral.strategy;
//
//public class StrategyPatternCheck {
//	public static void main(String[] args) {
//		String character = "optimist";
//		BusinessPlanPredictor businessPredictor;
//		if (character.equals("optimist")) {
//			businessPredictor = new BusinessPlanPredictor(new ProfitableCalculationStrategy());
//		} else {
//			businessPredictor = new BusinessPlanPredictor(new SurviveCalculationStrategy());
//		}
//		businessPredictor.makeAPrediction(1, 2);
//	}
//}
//
//class BusinessPlanPredictor {
//	private CalculationStrategy calculationStrategy;
//	public BusinessPlanPredictor(CalculationStrategy calculationStrategy) {
//		this.calculationStrategy = calculationStrategy;
//	}
//	public void makeAPrediction(PredictionStrategy predictionStrategy) {
//		this.calculationStrategy.execute(value1, value2);
//	}
//}
//
//interface CalculationStrategy {
//	int execute(int firstValue, int secondValue);
//}
//
//class ProfitableCalculationStrategy implements CalculationStrategy {
//	public int execute(int firstValue, int secondValue) {
//		int result = firstValue + secondValue;
//		System.out.println("profit - " + result );
//		return result;
//	}
//}
//
//class SurviveCalculationStrategy implements CalculationStrategy {
//	public int execute(int firstValue, int secondValue) {
//		System.out.println("surviving - " + 100);
//		return 100;
//	}
//}