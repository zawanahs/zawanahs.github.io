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
          type: 'emphasis',
          children: [{ type: 'text', value: caption }],
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
