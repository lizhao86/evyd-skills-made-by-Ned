# Output Channel Config

## Active Channel

```
active: feishu
```

改这一行即可切换全部 skill 的输出渠道。可选值：`feishu` · `obsidian` · `local-markdown`

---

## Channel: feishu

### Write Protocol（强制执行，不可跳过）

1. `feishu_doc.create` — 只创建文档壳，**不在 create payload 里塞正文**
2. `feishu_doc.read` — 立即验证文档可访问
3. `feishu_doc.write` — 全量写入正文
4. 若第 3 步产出空文档或报错 → 拆分成更短的结构化内容，改用 `feishu_doc.append` 逐段写入
5. `feishu_doc.read` — 最终验证文档非空

### Format Constraints（飞书渲染器限制）

- ✅ 标题（H1/H2/H3）、段落、bullet list、有序列表
- ❌ **禁止 Markdown 表格** — 飞书不渲染
- ❌ 禁止超过 2 层的复杂嵌套
- ❌ 避免超长连续段落
- 推荐结构：`H1 → H2 → bullet list`

### File Naming Convention

```
For {User昵称} - {Type} - {Title} - {YYYYMMDD}
```

- `{User昵称}` — 优先用飞书可读显示名；无法获取时 fallback 到对话上下文中的可读名；**不得使用** open_id / user_id / 系统标识
- `{Type}` — 由各 skill 自定义（如 👊「Research」、「UserStory」、「Manual」）
- `{Title}` — 从内容派生的简短标题
- `{YYYYMMDD}` — 创建日期

### Default Folder

各 skill 在自己的 `SKILL.md` 里声明 `folder_token`。Output Channel 不做全局绑定，方便不同 skill 输出到不同目录。

---

## Channel: obsidian

### Config（使用前必填）

```
obsidian_vault_path: /path/to/your/vault/output-folder
```

将此路径替换为实际 Obsidian vault 的目标文件夹绝对路径。

### Write Protocol

1. 拼接完整文件路径：`{obsidian_vault_path}/{filename}.md`
2. 用本地文件写入工具一次性写入全部正文（无需分块，无"空文档"问题）
3. 用本地文件读取工具验证文件存在且非空

### Format Constraints

- ✅ 完整 Markdown，**包括表格**
- ✅ 支持 Wikilink `[[...]]`
- ✅ 支持 frontmatter（YAML `---` 块）
- 无渲染器限制，feishu 的"禁止表格"约束在此渠道不适用

### File Naming Convention

```
For {User} - {Type} - {Title} - {YYYYMMDD}.md
```

- `{User}` — 使用对话中的可读名称
- `{Type}` / `{Title}` / `{YYYYMMDD}` — 与 feishu 规则一致

---

## Channel: local-markdown

### Config（使用前必填）

```
local_output_path: /path/to/output/folder
```

### Write Protocol

1. 拼接完整文件路径：`{local_output_path}/{filename}.md`
2. 用本地文件写入工具一次性写入全部正文
3. 用本地文件读取工具验证文件存在且非空

### Format Constraints

- ✅ 完整 Markdown，**包括表格**
- 无渲染器限制

### File Naming Convention

```
For {User} - {Type} - {Title} - {YYYYMMDD}.md
```
