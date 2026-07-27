const emoticons = [
  { token: ':3', emoji: '😺' },
  { token: ':)', emoji: '🙂' },
  { token: ':D', emoji: '😄' },
  { token: ';)', emoji: '😉' },
  { token: ':(', emoji: '🙁' },
];

const skippedParents = new Set(['code', 'inlineCode', 'link', 'linkReference', 'definition']);
const boundaryBefore = String.raw`(^|[\s([{\"'“‘.,!?;])`;
const boundaryAfter = String.raw`(?=$|[\s)\]}\"'”’.,!?;])`;

export default function remarkEmoticons() {
  return (tree) => transformText(tree);
}

function transformText(node, parentType = '') {
  if (node.type === 'text' && !skippedParents.has(parentType)) {
    for (const { token, emoji } of emoticons) {
      const escapedToken = token.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const pattern = new RegExp(`${boundaryBefore}${escapedToken}${boundaryAfter}`, 'g');
      node.value = node.value.replace(pattern, (_match, prefix) => `${prefix}${emoji}`);
    }
  }

  if (!Array.isArray(node.children)) return;
  for (const child of node.children) transformText(child, node.type);
}
