#!/bin/bash
# 重新打包 evyd-skills.plugin
# 用法：在 git pull 之后运行此脚本，然后在 Cowork 重新安装 .plugin 文件

set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT="$REPO_DIR/evyd-skills.plugin"
TMP_DIR="/tmp/evyd-skills-plugin-build"

echo "📦 重新打包 evyd-skills.plugin ..."

# 清理临时目录
rm -rf "$TMP_DIR"
mkdir -p "$TMP_DIR/evyd-skills-plugin/.claude-plugin"
mkdir -p "$TMP_DIR/evyd-skills-plugin/skills"

# 复制 plugin 配置
cp "$REPO_DIR/.claude-plugin/plugin.json" "$TMP_DIR/evyd-skills-plugin/.claude-plugin/plugin.json"
cp "$REPO_DIR/README.md" "$TMP_DIR/evyd-skills-plugin/README.md" 2>/dev/null || true

# 复制所有技能
for skill_dir in "$REPO_DIR"/*/; do
  skill_name=$(basename "$skill_dir")
  if [ -f "$skill_dir/SKILL.md" ]; then
    cp -r "$skill_dir" "$TMP_DIR/evyd-skills-plugin/skills/$skill_name"
    echo "  ✓ $skill_name"
  fi
done

# 打包
cd "$TMP_DIR"
zip -r "$OUTPUT" evyd-skills-plugin -x "*.DS_Store" -x "__pycache__/*" -x "*.pyc" -q
echo ""
echo "✅ 打包完成：$OUTPUT"
echo "   请在 Cowork 中重新安装此文件以更新技能。"
