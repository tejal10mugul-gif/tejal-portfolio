// Tejal Mugul — Opportunity Scoring
// n8n Code node / JavaScript concept.
// Input: one normalized opportunity per item.

const weights = {
  roleFit: 25,
  skillFit: 20,
  experienceFit: 15,
  consultingRelevance: 15,
  locationFit: 10,
  sourceQuality: 10,
  recency: 5
};

function clamp(value) {
  return Math.max(0, Math.min(100, Number(value) || 0));
}

return $input.all().map(item => {
  const x = item.json;

  const score =
    clamp(x.roleFit) * weights.roleFit / 100 +
    clamp(x.skillFit) * weights.skillFit / 100 +
    clamp(x.experienceFit) * weights.experienceFit / 100 +
    clamp(x.consultingRelevance) * weights.consultingRelevance / 100 +
    clamp(x.locationFit) * weights.locationFit / 100 +
    clamp(x.sourceQuality) * weights.sourceQuality / 100 +
    clamp(x.recency) * weights.recency / 100;

  const priority =
    score >= 85 ? "Priority application" :
    score >= 70 ? "Strong match" :
    score >= 55 ? "Review" :
    "Low priority";

  return {
    json: {
      ...x,
      matchScore: Math.round(score),
      priority
    }
  };
});
