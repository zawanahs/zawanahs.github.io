const skippedParents = new Set(['code', 'inlineCode', 'link', 'linkReference', 'definition']);

export default function remarkTypography() {
  return (tree) => transformText(tree);
}

function transformText(node, parentType = '') {
  if (node.type === 'text' && !skippedParents.has(parentType)) {
    node.value = node.value.replace(/->/g, '→');
  }

  if (!Array.isArray(node.children)) return;
  for (const child of node.children) transformText(child, node.type);
}
