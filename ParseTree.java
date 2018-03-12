public class BinaryOperation{
	/*
	* The operator symbol used for addition
	*/
	public static final String ADD

	/*
	* The operator symbol used for subtraction
	*/
	public static final String SUB

	/*
	* The operator symbol used for multiplication
	*/
	public static final String MUL

	/*
	* The operator symbol used for division
	*/
	public static final String DIV

	/*
	* Container of all legal binary operators, for use by parsers
	*/
	public static final java.util.Collection<String> OPERATORS

	/*
	* Compute the result of evaluating both operands and applying the operator to them.
	*/
	public int evaluate(java.util.Map<String,Integer> symTab){ return 0; }

	/*
	* Print, on standard output, the infixDisplay of the two child nodes separated by the operator and surrounded by parentheses. Blanks are inserted throughout.
	*/
	public void infixDisplay(){}

	/*
	* Emit the Machine instructions necessary to perform the computation of this BinaryOperation. The operator itself is realized by an instruction that pops two values off the stack, applies the operator, and pushes the answer.
	*/
	public java.util.List<Machine.Instruction> emit(){ return null; }

}