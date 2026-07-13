function Pandoc(doc)
  -- Build a bullet list TOC from level-1 and level-2 headers
  local items = {}
  for _, blk in ipairs(doc.blocks) do
    if blk.t == "Header" and (blk.level == 1 or blk.level == 2) then
      local text = pandoc.utils.stringify(blk)
      local id = blk.identifier
      local link = pandoc.Link(text, "#" .. id)
      table.insert(items, {level = blk.level, link = link})
    end
  end

  -- Build nested list structure
  local toc_blocks = {}
  local h1_list = {}
  local i = 1
  while i <= #items do
    local it = items[i]
    if it.level == 1 then
      -- gather following h2s
      local subs = {}
      local j = i + 1
      while j <= #items and items[j].level == 2 do
        table.insert(subs, pandoc.Plain({items[j].link}))
        j = j + 1
      end
      local h1_item = { pandoc.Plain({it.link}) }
      if #subs > 0 then
        table.insert(h1_item, pandoc.BulletList(subs))
      end
      table.insert(h1_list, h1_item)
      i = j
    else
      i = i + 1
    end
  end

  local toc_div = pandoc.Div({ pandoc.BulletList(h1_list) }, pandoc.Attr("TOC", {}, {}))

  -- Insert TOC after the first block (the cover div)
  local newblocks = {}
  table.insert(newblocks, doc.blocks[1])  -- cover
  table.insert(newblocks, toc_div)        -- toc
  for k = 2, #doc.blocks do
    table.insert(newblocks, doc.blocks[k])
  end

  return pandoc.Pandoc(newblocks, doc.meta)
end
