/* ============================================================
 *  HNS Coordinate System + Layer Alignment OS
 *  (Specification + Skeleton Implementation)
 * ============================================================ */

/* ------------------------------
 *  Core Types
 * ------------------------------ */

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
 *  User Coordinate Decision
 * ------------------------------ */

/**
 * decideUserCoordinate()
 * Determine the coordinate (L, C, A/G, R/F) of a user utterance.
 */
export function decideUserCoordinate(
  u: Utterance,
  h: History
): Coordinate {
  const span = selectContextSpan(h, u);
  const layer = decideLayer(span, u);
  const category = decideCategory(span, u);
  const abstraction = decideAbstraction(span, u);
  const granularity = decideGranularity(span, u);

  return { layer, category, abstraction, granularity };
}

/**
 * selectContextSpan()
 * Extract the continuous context segment.
 */
export function selectContextSpan(h: History, u: Utterance): History {
  // TODO: implement continuity rules
  return h;
}

/**
 * decideLayer()
 * Determine the causal layer of the utterance.
 */
export function decideLayer(span: History, u: Utterance): Layer {
  // TODO: implement layer rules
  return 'L5_SYSTEM';
}

/**
 * decideCategory()
 * Determine the cognitive operation of the utterance.
 */
export function decideCategory(span: History, u: Utterance): Category {
  // TODO: implement category rules
  return 'C3_MEANS';
}

/**
 * decideAbstraction()
 * Determine abstract vs concrete.
 */
export function decideAbstraction(span: History, u: Utterance): Abstraction {
  // TODO: implement abstraction rules
  return 'CONCRETE';
}

/**
 * decideGranularity()
 * Determine rough vs fine.
 */
export function decideGranularity(span: History, u: Utterance): Granularity {
  // TODO: implement granularity rules
  return 'ROUGH';
}

/* ------------------------------
 *  Layer Alignment OS
 * ------------------------------ */

export interface AIResponsePlan {
  user: Coordinate;
  ai: Coordinate;
}

/**
 * planResponse()
 * Integrated OS:
 *  Phase 1: decide user coordinate
 *  Phase 2: align AI layer to user layer
 *  Phase 3: generate AI coordinate
 */
export function planResponse(
  u: Utterance,
  h: History
): AIResponsePlan {
  const userCoord = decideUserCoordinate(u, h);
  const userLayer = userCoord.layer;

  // Layer alignment (AI must match user layer)
  let aiLayer: Layer = userLayer;

  // Optional: layer-shift logic (requires declaration)
  // TODO: implement if needed

  const aiCategory = decideResponseCategory(u, h, userCoord);
  const aiAbstraction = decideResponseAbstraction(u, h, userCoord);
  const aiGranularity = decideResponseGranularity(u, h, userCoord);

  return {
    user: userCoord,
    ai: {
      layer: aiLayer,
      category: aiCategory,
      abstraction: aiAbstraction,
      granularity: aiGranularity,
    },
  };
}

/**
 * Response coordinate decisions
 * (AI-side; L is fixed by alignment)
 */
export function decideResponseCategory(
  u: Utterance,
  h: History,
  user: Coordinate
): Category {
  // TODO: implement response category rules
  return user.category;
}

export function decideResponseAbstraction(
  u: Utterance,
  h: History,
  user: Coordinate
): Abstraction {
  // TODO: implement response abstraction rules
  return user.abstraction;
}

export function decideResponseGranularity(
  u: Utterance,
  h: History,
  user: Coordinate
): Granularity {
  // TODO: implement response granularity rules
  return user.granularity;
}
