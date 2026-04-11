/* ============================================================
 *  HNS Coordinate System OS - ComplexA (Linguistic-Based)
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
 *  ComplexA: Linguistic-Based Logic
 * ------------------------------ */

/**
 * decideLayerComplexA()
 * Determine layer using linguistic signals:
 * - keyword dictionaries
 * - syntactic structure
 * - semantic roles
 * - discourse markers
 */
export function decideLayerComplexA(
  span: History,
  u: Utterance
): Layer {
  const text = u.text;

  /* --------------------------------------------------
   * 1. Keyword dictionaries (fast path)
   * -------------------------------------------------- */
  if (contains(text, BODY_WORDS)) return 'L1_BODY';
  if (contains(text, EMOTION_WORDS)) return 'L2_EMOTION';
  if (contains(text, ACTION_WORDS)) return 'L3_ACTION';
  if (contains(text, RELATION_WORDS)) return 'L4_RELATION';
  if (contains(text, SYSTEM_WORDS)) return 'L5_SYSTEM';
  if (contains(text, VALUE_WORDS)) return 'L6_VALUE';

  /* --------------------------------------------------
   * 2. Syntactic analysis
   * -------------------------------------------------- */
  const syntax = parseSyntax(text);

  if (syntax.mainPredicateType === 'INTENT') return 'L3_ACTION';
  if (syntax.mainPredicateType === 'EVALUATION') return 'L6_VALUE';

  /* --------------------------------------------------
   * 3. Semantic role labeling
   * -------------------------------------------------- */
  const roles = semanticRoles(text);

  if (roles.topic === 'SELF_EMOTION') return 'L2_EMOTION';
  if (roles.topic === 'OTHER_PERSON') return 'L4_RELATION';
  if (roles.topic === 'SYSTEM') return 'L5_SYSTEM';

  /* --------------------------------------------------
   * 4. Discourse markers
   * -------------------------------------------------- */
  if (startsWith(text, ['しかし', 'でも', 'ところで'])) {
    const prev = lastLayer(span);
    return prev;
  }

  /* --------------------------------------------------
   * 5. Fallback
   * -------------------------------------------------- */
  return 'L3_ACTION';
}

/* ------------------------------
 *  Category / Abstraction / Granularity
 * ------------------------------ */

export function decideCategoryComplexA(
  span: History,
  u: Utterance
): Category {
  const text = u.text;

  if (contains(text, GOAL_MARKERS)) return 'C2_GOAL';
  if (contains(text, MEANS_MARKERS)) return 'C3_MEANS';
  if (contains(text, CONDITION_MARKERS)) return 'C4_CONDITION';
  if (contains(text, CONSTRAINT_MARKERS)) return 'C5_CONSTRAINT';
  if (contains(text, VALUE_MARKERS)) return 'C6_VALUE';

  return 'C1_TARGET';
}

export function decideAbstractionComplexA(
  span: History,
  u: Utterance
): Abstraction {
  const text = u.text;
  if (contains(text, ABSTRACT_WORDS)) return 'ABSTRACT';
  return 'CONCRETE';
}

export function decideGranularityComplexA(
  span: History,
  u: Utterance
): Granularity {
  const text = u.text;
  if (contains(text, FINE_DETAIL_WORDS)) return 'FINE';
  return 'ROUGH';
}

/* ------------------------------
 *  User Coordinate (ComplexA)
 * ------------------------------ */

export function decideUserCoordinateComplexA(
  u: Utterance,
  h: History
): Coordinate {
  const span = h;

  const layer = decideLayerComplexA(span, u);
  const category = decideCategoryComplexA(span, u);
  const abstraction = decideAbstractionComplexA(span, u);
  const granularity = decideGranularityComplexA(span, u);

  return { layer, category, abstraction, granularity };
}

/* ------------------------------
 *  Utility placeholders
 * ------------------------------ */

function contains(text: string, list: string[]): boolean {
  return list.some(w => text.includes(w));
}

function parseSyntax(text: string): any {
  return { mainPredicateType: 'ACTION' };
}

function semanticRoles(text: string): any {
  return { topic: 'ACTION' };
}

function lastLayer(span: History): Layer {
  return 'L3_ACTION';
}

/* ------------------------------
 *  Dictionaries (placeholder)
 * ------------------------------ */

const BODY_WORDS = ['体', '疲れ', '痛み'];
const EMOTION_WORDS = ['悲しい', '嬉しい', '不安'];
const ACTION_WORDS = ['する', 'したい', 'やる'];
const RELATION_WORDS = ['相手', '友達', '上司'];
const SYSTEM_WORDS = ['制度', '仕組み', 'ルール'];
const VALUE_WORDS = ['正しい', '間違い', '良い', '悪い'];

const GOAL_MARKERS = ['したい', '目標', '目的'];
const MEANS_MARKERS = ['ために', '手段', '方法'];
const CONDITION_MARKERS = ['なら', '場合', 'もし'];
const CONSTRAINT_MARKERS = ['できない', '禁止', '制限'];
const VALUE_MARKERS = ['良い', '悪い', 'べき'];

const ABSTRACT_WORDS = ['概念', '抽象', '一般的'];
const FINE_DETAIL_WORDS = ['具体的', '詳細', '細かい'];
