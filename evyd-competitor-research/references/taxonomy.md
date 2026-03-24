# System & Module 归类指南

文档命名时，AI 根据调研内容从以下分类中选择最匹配项。

## System（系统层面）

有组织的、相互关联的元素集合（物理+数字），为特定目的协同工作。

| ID | 名称 | 说明 |
|---|---|---|
| HealthInformationExchange | 健康信息交换系统 | 跨机构健康数据共享 |
| ClinicalDecisionSupport | 临床决策支持系统 | 辅助临床决策的智能系统 |
| PopulationHealthManagement | 人群健康管理系统 | 面向群体的健康管理与干预 |
| ElectronicHealthRecord | 电子病历系统 | 电子化病历管理 |
| TelehealthPlatform | 远程医疗平台 | 远程问诊/监测平台 |
| RevenueCycleManagement | 收入周期管理系统 | 医疗机构财务/收入管理 |
| PatientEngagement | 患者参与系统 | 患者沟通/互动平台 |
| SupplyChainManagement | 供应链管理系统 | 医疗物资/供应链管理 |

## Module（模块层面）

系统或产品内的自包含单元，专注于特定功能，可独立运行。

| ID | 名称 | 说明 |
|---|---|---|
| InteroperabilityLayer | 互操作层模块 | FHIR/HL7/API 集成 |
| AnalyticsEngine | 分析引擎模块 | 数据分析/BI/报表 |
| PatientPortal | 患者门户模块 | 患者自助服务入口 |
| ProviderPortal | 医生门户模块 | 医生工作台 |
| BillingModule | 计费模块 | 费用计算/结算 |
| SchedulingModule | 排班模块 | 排班/预约管理 |
| ReportingModule | 报表模块 | 报表生成/输出 |
| IntegrationAPI | 集成 API 模块 | 对外集成接口 |

## 归类原则

1. 优先匹配竞品的**主营业务**，而非某个子功能
2. 一个竞品可能横跨多个 System，选最核心的那个
3. Module 选竞品**最突出的差异化模块**
4. 拿不准时标注【AI 归类】，用户可修正
