export default function remarkFigureCaptions() {
  return (tree) => {
    transformChildren(tree);
  };
}

function transformChildren(node) {
  if (!Array.isArray(node.children)) return;

  for (const child of node.children) {
    if (
      child.type === 'paragraph' &&
      child.children?.length === 1 &&
      child.children[0].type === 'image' &&
      child.children[0].title
    ) {
      const image = child.children[0];
      const caption = image.title.trim();

      image.title = null;
      child.data = {
        ...child.data,
        hName: 'figure',
        hProperties: { className: ['article-figure'] },
      };
      child.children = [
        image,
        {
          type: 'paragraph',
          children: parseCaption(caption),
          data: {
            hName: 'figcaption',
            hProperties: { className: ['article-caption'] },
          },
        },
      ];
    }

    transformChildren(child);
  }
}

function parseCaption(value) {
  const children = [];
  const inlinePattern = /\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)|\*([^*]+)\*/g;
  let cursor = 0;
  let match;

  while ((match = inlinePattern.exec(value)) !== null) {
    if (match.index > cursor) {
      children.push({ type: 'text', value: value.slice(cursor, match.index) });
    }

    if (match[1] && match[2]) {
      children.push({
        type: 'link',
        url: match[2],
        children: [{ type: 'text', value: match[1] }],
      });
    } else {
      children.push({
        type: 'emphasis',
        children: [{ type: 'text', value: match[3] }],
      });
    }

    cursor = inlinePattern.lastIndex;
  }

  if (cursor < value.length) {
    children.push({ type: 'text', value: value.slice(cursor) });
  }

  return children;
}
