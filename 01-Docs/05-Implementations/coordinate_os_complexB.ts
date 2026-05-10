/* ============================================================
 *  HNS Coordinate System OS - ComplexB (Causal-Line Based)
 *  (Specification + Skeleton Implementation)
 * ============================================================ */

export type Layer =
  | 'L1_BODY'
  | 'L2_EMOTION'
  | 'L3_ACTION'
  | 'L4_RELATION'
  | 'L5_SYSTEM'
  | 'L6_VALUE';

export type Category =
  | 'C1_TARGET'
  | 'C2_GOAL'
  | 'C3_MEANS'
  | 'C4_CONDITION'
  | 'C5_CONSTRAINT'
  | 'C6_VALUE';

export type Abstraction = 'ABSTRACT' | 'CONCRETE';
export type Granularity = 'ROUGH' | 'FINE';

export interface Coordinate {
  layer: Layer;
  category: Category;
  abstraction: Abstraction;
  granularity: Granularity;
}

export interface Utterance {
  text: string;
}

export type History = Utterance[];

/* ------------------------------
 *  ComplexB: Causal-Line Based Logic
 * ------------------------------ */

/**
 * decideLayerComplexB()
 * Determine layer by causal source, target, focus, and grain.
 */
export function decideLayerComplexB(
  span: History,
  u: Utterance
): Layer {
  const text = u.text;

  const source = detectCausalSource(text);
  const target = detectCausalTarget(text);
  const focus = determineCausalFocus(source, target);
  const grain = detectCausalGrain(text);

  if (grain === 'MICRO' && focus === 'BODY') return 'L1_BODY';
  if (grain === 'MICRO' && focus === 'EMOTION') return 'L2_EMOTION';
  if (grain === 'MICRO' && focus === 'ACTION') return 'L3_ACTION';
  if (grain === 'MESO') return 'L4_RELATION';
  if (grain === 'MACRO' && focus === 'SYSTEM') return 'L5_SYSTEM';
  if (grain === 'MACRO' && focus === 'VALUE') return 'L6_VALUE';

  return 'L3_ACTION';
}

/* ------------------------------
 *  Placeholder functions
 * ------------------------------ */

export function detectCausalSource(text: string): string {
  // TODO: implement causal source detection
  return 'ACTION';
}

export function detectCausalTarget(text: string): string {
  // TODO: implement causal target detection
  return 'SELF';
}

export function determineCausalFocus(
  source: string,
  target: string
): string {
  // TODO: implement causal focus logic
  return 'ACTION';
}

export function detectCausalGrain(text: string): string {
  // TODO: implement causal grain detection
  return 'MICRO';
}

/* ------------------------------
 *  Category / Abstraction / Granularity
 * ------------------------------ */

export function decideCategoryComplexB(
  span: History,
  u: Utterance
): Category {
  // TODO: implement causal-based category logic
  return 'C3_MEANS';
}

export function decideAbstractionComplexB(
  span: History,
  u: Utterance
): Abstraction {
  return 'CONCRETE';
}

export function decideGranularityComplexB(
  span: History,
  u: Utterance
): Granularity {
  return 'ROUGH';
}

/* ------------------------------
 *  User Coordinate (ComplexB)
 * ------------------------------ */

export function decideUserCoordinateComplexB(
  u: Utterance,
  h: History
): Coordinate {
  const span = h;
  const layer = decideLayerComplexB(span, u);
  const category = decideCategoryComplexB(span, u);
  const abstraction = decideAbstractionComplexB(span, u);
  const granularity = decideGranularityComplexB(span, u);

  return { layer, category, abstraction, granularity };
}
