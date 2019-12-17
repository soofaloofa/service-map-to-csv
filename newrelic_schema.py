import sgqlc.types
import sgqlc.types.datetime


newrelic_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class AgentReleasesFilter(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('ANDROID', 'BROWSER', 'DOTNET', 'ELIXIR', 'GO', 'INFRASTRUCTURE', 'IOS', 'JAVA', 'NODEJS', 'PHP', 'PYTHON', 'RUBY', 'SDK')


class AlertsIncidentPreference(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('PER_CONDITION', 'PER_CONDITION_AND_TARGET', 'PER_POLICY')


class AlertsMutingRuleConditionAttribute(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('ACCOUNT_ID', 'ALERTS_CONDITION_ID', 'ALERTS_CONDITION_NAME', 'ALERTS_CONDITION_RUNBOOK_URL', 'ALERTS_CONDITION_TYPE', 'ALERTS_POLICY_ID', 'ALERTS_POLICY_NAME', 'ALERTS_TARGET_ID', 'ALERTS_TARGET_NAME', 'NRQL_EVENT_TYPE', 'NRQL_FACET', 'NRQL_QUERY', 'PRODUCT')


class AlertsMutingRuleConditionGroupOperator(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('AND', 'OR')


class AlertsMutingRuleConditionOperator(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('ANY', 'CONTAINS', 'ENDS_WITH', 'EQUALS', 'IN', 'IS_BLANK', 'IS_NOT_BLANK', 'NOT_CONTAINS', 'NOT_ENDS_WITH', 'NOT_EQUALS', 'NOT_IN', 'NOT_STARTS_WITH', 'STARTS_WITH')


Boolean = sgqlc.types.Boolean

class ChartFormatType(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('PDF', 'PNG')


class ChartImageType(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('APDEX', 'AREA', 'BAR', 'BASELINE', 'BILLBOARD', 'BULLET', 'EVENT_FEED', 'FUNNEL', 'HEATMAP', 'HISTOGRAM', 'LINE', 'PIE', 'SCATTER', 'STACKED_HORIZONTAL_BAR', 'TABLE', 'VERTICAL_BAR')


Date = sgqlc.types.datetime.Date

DateTime = sgqlc.types.datetime.DateTime

class DistributedTracingSpanAnomalyType(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('DURATION',)


class DistributedTracingSpanAttributes(sgqlc.types.Scalar):
    __schema__ = newrelic_schema


class DistributedTracingSpanClientType(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('DATASTORE', 'EXTERNAL')


class DistributedTracingSpanProcessBoundary(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('ENTRY', 'EXIT', 'IN_PROCESS')


class EmbeddedChartType(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('APDEX', 'AREA', 'BAR', 'BASELINE', 'BILLBOARD', 'BULLET', 'EMPTY', 'EVENT_FEED', 'FUNNEL', 'HEATMAP', 'HISTOGRAM', 'JSON', 'LINE', 'MARKDOWN', 'PIE', 'SCATTER', 'STACKED_HORIZONTAL_BAR', 'TABLE', 'TRAFFIC_LIGHT', 'VERTICAL_BAR')


class EntityAlertSeverity(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('CRITICAL', 'NOT_ALERTING', 'NOT_CONFIGURED', 'WARNING')


class EntityGuid(sgqlc.types.Scalar):
    __schema__ = newrelic_schema


class EntityInfrastructureIntegrationType(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('REDIS_INSTANCE', 'AWS_ELASTIC_BEANSTALK_INSTANCE', 'KAFKA_TOPIC', 'NA', 'AWS_LAMBDA_REGION', 'AZURE_LOAD_BALANCER_BACKEND', 'AWS_ROUTE53_HEALTH_CHECK', 'AZURE_SERVICE_BUS_TOPIC', 'AZURE_SERVICE_BUS_QUEUE', 'GCP_KUBERNETES_NODE', 'AWS_IAM_OPEN_ID_PROVIDER', 'AWS_VPC_SUBNET', 'AWS_IAM_ROLE', 'AWS_ELASTI_CACHE_MEMCACHED_NODE', 'AWS_VPC_VPN_CONNECTION', 'AWS_VPC_NAT_GATEWAY', 'GCP_SPANNER_INSTANCE', 'AWS_VPC_NETWORK_ACL', 'GCP_CLOUD_FUNCTION', 'F5_POOL_MEMBER', 'AZURE_VIRTUAL_NETWORKS_IP_CONFIGURATION', 'F5_VIRTUAL_SERVER', 'AZURE_SERVICE_BUS_SUBSCRIPTION', 'AWS_VPC_PEERING_CONNECTION', 'AZURE_STORAGE_ACCOUNT', 'AWS_IAM_VIRTUAL_MFA_DEVICE', 'AWS_LAMBDA_FUNCTION_ALIAS', 'AWS_VPC_VPN_TUNNEL', 'AZURE_SQL_ELASTIC_POOL', 'AZURE_SQL_RESTORE_POINT', 'F5_NODE', 'AWS_LAMBDA_AGENT_TRANSACTION', 'GCP_INTERNAL_LOAD_BALANCER', 'ORACLE_DB_INSTANCE', 'RABBIT_MQ_CLUSTER', 'AWS_HEALTH_NOTIFICATION', 'MEMCACHED_INSTANCE', 'POSTGRE_SQL_INSTANCE', 'KUBERNETES_CLUSTER', 'F5_SYSTEM', 'AWS_LAMBDA_EDGE_FUNCTION', 'AWS_S3_BUCKET', 'AWS_DYNAMO_DB_GLOBAL_SECONDARY_INDEX', 'AWS_IAM_SERVER_CERTIFICATE', 'AWS_AUTO_SCALING_GROUP', 'AWS_VPC_ROUTE_TABLE', 'AWS_HEALTH_UNKNOWN', 'AZURE_LOAD_BALANCER_PROBE', 'AWS_KINESIS_DELIVERY_STREAM', 'F5_POOL', 'GCP_KUBERNETES_CONTAINER', 'AZURE_LOAD_BALANCER_FRONTEND_IP', 'AWS_ALB_LISTENER_RULE', 'AWS_ECS_CLUSTER', 'AZURE_POSTGRESQL_SERVER', 'RABBIT_MQ_QUEUE', 'CASSANDRA_NODE', 'AZURE_VIRTUAL_NETWORKS_ROUTE_TABLE', 'AWS_ELASTICSEARCH_CLUSTER', 'AWS_ALB_LISTENER', 'AWS_ECS_SERVICE', 'AZURE_LOAD_BALANCER_INBOUND_NAT_RULE', 'AZURE_VIRTUAL_NETWORKS_PUBLIC_IP_ADDRESS', 'AWS_IAM_GROUP', 'AWS_ELASTI_CACHE_MEMCACHED_CLUSTER', 'AWS_HEALTH_SCHEDULED_CHANGE', 'AWS_S3_BUCKET_REQUESTS', 'AWS_SNS_SUBSCRIPTION', 'GCP_PUB_SUB_TOPIC', 'AWS_VPC_ENDPOINT', 'AZURE_COSMOS_DB_ACCOUNT', 'AWS_BILLING_SERVICE_COST', 'AWS_SES_RECEIPT_FILTER', 'AWS_ALB_TARGET_GROUP', 'AWS_AUTO_SCALING_POLICY', 'AWS_EBS_VOLUME', 'COUCHBASE_QUERY_ENGINE', 'AWS_VPC', 'AWS_SES_RECEIPT_RULE', 'AWS_IOT_BROKER', 'AWS_LAMBDA_FUNCTION', 'AWS_SES_EVENT_DESTINATION', 'AWS_AUTO_SCALING_INSTANCE', 'GCP_KUBERNETES_POD', 'MSSQL_INSTANCE', 'AZURE_LOAD_BALANCER_RULE', 'AZURE_SQL_REPLICATION_LINK', 'AWS_KINESIS_STREAM', 'AWS_ROUTE53_ZONE', 'AWS_IOT_RULE', 'GCP_CLOUD_TASKS_QUEUE', 'GCP_PUB_SUB_SUBSCRIPTION', 'GCP_BIG_QUERY_PROJECT', 'AWS_RDS_DB_INSTANCE', 'AWS_VPC_SECURITY_GROUP', 'AWS_API_GATEWAY_API', 'AWS_BILLING_ACCOUNT_COST', 'AWS_ELASTICSEARCH_INSTANCE', 'AWS_ELASTIC_MAP_REDUCE_INSTANCE_GROUP', 'AWS_ELASTIC_MAP_REDUCE_INSTANCE', 'AWS_HEALTH_ISSUE', 'AWS_BILLING_ACCOUNT_SERVICE_COST', 'AWS_API_GATEWAY_RESOURCE_WITH_METRICS', 'AZURE_LOAD_BALANCER', 'AWS_CLOUD_FRONT_DISTRIBUTION', 'CONSUL_AGENT', 'AZURE_SQL_SERVER', 'AWS_SNS_TOPIC', 'AZURE_APP_SERVICE_WEB_APP', 'GCP_SPANNER_DATABASE', 'GCP_BIG_QUERY_DATA_SET', 'AZURE_SQL_FIREWALL', 'AZURE_VIRTUAL_NETWORKS_PEERING', 'AWS_LAMBDA_TRACE', 'AWS_EFS_FILE_SYSTEM', 'ELASTICSEARCH_NODE', 'AWS_KINESIS_STREAM_SHARD', 'AWS_VPC_INTERNET_GATEWAY', 'KAFKA_BROKER', 'GCP_TCP_SSL_PROXY_LOAD_BALANCER', 'AWS_CLOUD_TRAIL', 'AZURE_REDIS_CACHE_SHARD', 'AZURE_MYSQL_SERVER', 'GCP_STORAGE_BUCKET', 'GCP_CLOUD_SQL', 'AWS_LAMBDA_SPAN', 'AWS_LAMBDA_AGENT_TRANSACTION_ERROR', 'GCP_HTTP_LOAD_BALANCER', 'AZURE_VIRTUAL_NETWORKS_ROUTE', 'AWS_SES_RECEIPT_RULE_SET', 'AWS_SES_REGION', 'GCP_BIG_QUERY_TABLE', 'AWS_ELASTIC_MAP_REDUCE_INSTANCE_FLEET', 'AWS_ROUTE53_ZONE_RECORD_SET', 'AWS_ALB', 'AWS_SQS_QUEUE', 'AZURE_VIRTUAL_NETWORKS_NETWORK_INTERFACE', 'AZURE_FUNCTIONS_APP', 'AWS_ELASTIC_BEANSTALK_ENVIRONMENT', 'MYSQL_NODE', 'AZURE_VIRTUAL_NETWORKS', 'AZURE_VIRTUAL_NETWORKS_SECURITY_GROUP', 'COUCHBASE_BUCKET', 'GCP_VIRTUAL_MACHINE_DISK', 'AWS_IAM_POLICY', 'COUCHBASE_CLUSTER', 'AWS_ELB', 'AWS_LAMBDA_OPERATION', 'VARNISH_INSTANCE', 'AWS_AUTO_SCALING_LAUNCH_CONFIGURATION', 'RABBIT_MQ_EXCHANGE', 'AZURE_VIRTUAL_NETWORKS_SUBNET', 'AWS_ELASTIC_MAP_REDUCE_CLUSTER', 'AWSELASTICSEARCHNODE', 'AZURE_LOAD_BALANCER_INBOUND_NAT_POOL', 'AWS_ELASTI_CACHE_REDIS_NODE', 'AZURE_SERVICE_BUS_NAMESPACE', 'AWS_API_GATEWAY_STAGE', 'APACHE_SERVER', 'AWS_VPC_NETWORK_INTERFACE', 'AWS_BILLING_BUDGET', 'AWS_IAM_USER', 'AWS_RDS_DB_CLUSTER', 'COUCHBASE_NODE', 'AWS_DYNAMO_DB_REGION', 'AWS_ELASTI_CACHE_REDIS_CLUSTER', 'NGINX_SERVER', 'RABBIT_MQ_NODE', 'AZURE_VIRTUAL_NETWORKS_SECURITY_RULE', 'AZURE_SQL_DATABASE', 'AWS_SES_CONFIGURATION_SET', 'AWS_LAMBDA_EVENT_SOURCE_MAPPING', 'AWS_REDSHIFT_CLUSTER', 'AWS_AUTO_SCALING_REGION_LIMIT', 'AWS_REDSHIFT_NODE', 'AZURE_REDIS_CACHE', 'AWS_IOT_RULE_ACTION', 'AWS_DYNAMO_DB_TABLE', 'AWS_IAM', 'GCP_APP_ENGINE_SERVICE', 'AWS_IAM_SAML_PROVIDER', 'AZURE_APP_SERVICE_HOST_NAME', 'AWS_API_GATEWAY_RESOURCE', 'AZURE_MARIADB_SERVER')


class EntityRelationshipType(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('CALLS', 'CONTAINS', 'HOSTS', 'SERVES', 'UNKNOWN')


class EntitySearchQueryBuilderDomain(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('APM', 'BROWSER', 'INFRA', 'MOBILE', 'SYNTH')


class EntitySearchQueryBuilderType(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('APPLICATION', 'DASHBOARD', 'HOST', 'MONITOR')


class EntitySearchSortCriteria(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('ALERT_SEVERITY', 'DOMAIN', 'MOST_RELEVANT', 'NAME', 'REPORTING', 'TYPE')


class EntityType(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('APM_APPLICATION_ENTITY', 'APM_DATABASE_INSTANCE_ENTITY', 'APM_EXTERNAL_SERVICE_ENTITY', 'BROWSER_APPLICATION_ENTITY', 'DASHBOARD_ENTITY', 'GENERIC_ENTITY', 'GENERIC_INFRASTRUCTURE_ENTITY', 'INFRASTRUCTURE_AWS_LAMBDA_FUNCTION_ENTITY', 'INFRASTRUCTURE_HOST_ENTITY', 'MOBILE_APPLICATION_ENTITY', 'SYNTHETIC_MONITOR_ENTITY', 'UNAVAILABLE_ENTITY', 'WORKLOAD_ENTITY')


class EpochMilliseconds(sgqlc.types.Scalar):
    __schema__ = newrelic_schema


class EpochSeconds(sgqlc.types.Scalar):
    __schema__ = newrelic_schema


Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int

class Milliseconds(sgqlc.types.Scalar):
    __schema__ = newrelic_schema


class Minutes(sgqlc.types.Scalar):
    __schema__ = newrelic_schema


class NerdStorageDocument(sgqlc.types.Scalar):
    __schema__ = newrelic_schema


class NerdStorageScope(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('ACCOUNT', 'ACTOR', 'ENTITY')


class NrdbResult(sgqlc.types.Scalar):
    __schema__ = newrelic_schema


class Nrql(sgqlc.types.Scalar):
    __schema__ = newrelic_schema


class Seconds(sgqlc.types.Scalar):
    __schema__ = newrelic_schema


String = sgqlc.types.String

class SyntheticMonitorType(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('BROWSER', 'SCRIPT_API', 'SCRIPT_BROWSER', 'SIMPLE')


class TaggingMutationErrorType(sgqlc.types.Enum):
    __schema__ = newrelic_schema
    __choices__ = ('CONCURRENT_TASK_EXCEPTION', 'INVALID_DOMAIN_TYPE', 'INVALID_ENTITY_GUID', 'INVALID_KEY', 'INVALID_VALUE', 'NOT_FOUND', 'NOT_PERMITTED', 'TOO_MANY_TAG_KEYS', 'TOO_MANY_TAG_VALUES')



########################################################################
# Input Objects
########################################################################
class AlertsMutingRuleConditionGroupInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    conditions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AlertsMutingRuleConditionInput'))), graphql_name='conditions')
    operator = sgqlc.types.Field(sgqlc.types.non_null(AlertsMutingRuleConditionGroupOperator), graphql_name='operator')


class AlertsMutingRuleConditionInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    attribute = sgqlc.types.Field(sgqlc.types.non_null(AlertsMutingRuleConditionAttribute), graphql_name='attribute')
    attribute_param = sgqlc.types.Field(String, graphql_name='attributeParam')
    operator = sgqlc.types.Field(sgqlc.types.non_null(AlertsMutingRuleConditionOperator), graphql_name='operator')
    values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='values')


class AlertsMutingRuleInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    condition = sgqlc.types.Field(sgqlc.types.non_null(AlertsMutingRuleConditionGroupInput), graphql_name='condition')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class AlertsMutingRuleUpdateInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    condition = sgqlc.types.Field(AlertsMutingRuleConditionGroupInput, graphql_name='condition')
    description = sgqlc.types.Field(String, graphql_name='description')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    name = sgqlc.types.Field(String, graphql_name='name')


class CloudAlbIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    load_balancer_prefixes = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='loadBalancerPrefixes')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudApigatewayIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    stage_prefixes = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stagePrefixes')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudAutoscalingIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudAwsDisableIntegrationsInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    alb = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='alb')
    apigateway = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='apigateway')
    autoscaling = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='autoscaling')
    billing = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='billing')
    cloudfront = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='cloudfront')
    cloudtrail = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='cloudtrail')
    dynamodb = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='dynamodb')
    ebs = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='ebs')
    ec2 = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='ec2')
    ecs = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='ecs')
    efs = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='efs')
    elasticache = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='elasticache')
    elasticbeanstalk = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='elasticbeanstalk')
    elasticsearch = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='elasticsearch')
    elb = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='elb')
    emr = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='emr')
    health = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='health')
    iam = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='iam')
    iot = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='iot')
    kinesis = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='kinesis')
    kinesis_firehose = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='kinesisFirehose')
    lambda_ = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='lambda')
    rds = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='rds')
    redshift = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='redshift')
    route53 = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='route53')
    s3 = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='s3')
    ses = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='ses')
    sns = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='sns')
    sqs = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='sqs')
    vpc = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='vpc')


class CloudAwsIntegrationsInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    alb = sgqlc.types.Field(sgqlc.types.list_of(CloudAlbIntegrationInput), graphql_name='alb')
    apigateway = sgqlc.types.Field(sgqlc.types.list_of(CloudApigatewayIntegrationInput), graphql_name='apigateway')
    autoscaling = sgqlc.types.Field(sgqlc.types.list_of(CloudAutoscalingIntegrationInput), graphql_name='autoscaling')
    billing = sgqlc.types.Field(sgqlc.types.list_of('CloudBillingIntegrationInput'), graphql_name='billing')
    cloudfront = sgqlc.types.Field(sgqlc.types.list_of('CloudCloudfrontIntegrationInput'), graphql_name='cloudfront')
    cloudtrail = sgqlc.types.Field(sgqlc.types.list_of('CloudCloudtrailIntegrationInput'), graphql_name='cloudtrail')
    dynamodb = sgqlc.types.Field(sgqlc.types.list_of('CloudDynamodbIntegrationInput'), graphql_name='dynamodb')
    ebs = sgqlc.types.Field(sgqlc.types.list_of('CloudEbsIntegrationInput'), graphql_name='ebs')
    ec2 = sgqlc.types.Field(sgqlc.types.list_of('CloudEc2IntegrationInput'), graphql_name='ec2')
    ecs = sgqlc.types.Field(sgqlc.types.list_of('CloudEcsIntegrationInput'), graphql_name='ecs')
    efs = sgqlc.types.Field(sgqlc.types.list_of('CloudEfsIntegrationInput'), graphql_name='efs')
    elasticache = sgqlc.types.Field(sgqlc.types.list_of('CloudElasticacheIntegrationInput'), graphql_name='elasticache')
    elasticbeanstalk = sgqlc.types.Field(sgqlc.types.list_of('CloudElasticbeanstalkIntegrationInput'), graphql_name='elasticbeanstalk')
    elasticsearch = sgqlc.types.Field(sgqlc.types.list_of('CloudElasticsearchIntegrationInput'), graphql_name='elasticsearch')
    elb = sgqlc.types.Field(sgqlc.types.list_of('CloudElbIntegrationInput'), graphql_name='elb')
    emr = sgqlc.types.Field(sgqlc.types.list_of('CloudEmrIntegrationInput'), graphql_name='emr')
    health = sgqlc.types.Field(sgqlc.types.list_of('CloudHealthIntegrationInput'), graphql_name='health')
    iam = sgqlc.types.Field(sgqlc.types.list_of('CloudIamIntegrationInput'), graphql_name='iam')
    iot = sgqlc.types.Field(sgqlc.types.list_of('CloudIotIntegrationInput'), graphql_name='iot')
    kinesis = sgqlc.types.Field(sgqlc.types.list_of('CloudKinesisIntegrationInput'), graphql_name='kinesis')
    kinesis_firehose = sgqlc.types.Field(sgqlc.types.list_of('CloudKinesisFirehoseIntegrationInput'), graphql_name='kinesisFirehose')
    lambda_ = sgqlc.types.Field(sgqlc.types.list_of('CloudLambdaIntegrationInput'), graphql_name='lambda')
    rds = sgqlc.types.Field(sgqlc.types.list_of('CloudRdsIntegrationInput'), graphql_name='rds')
    redshift = sgqlc.types.Field(sgqlc.types.list_of('CloudRedshiftIntegrationInput'), graphql_name='redshift')
    route53 = sgqlc.types.Field(sgqlc.types.list_of('CloudRoute53IntegrationInput'), graphql_name='route53')
    s3 = sgqlc.types.Field(sgqlc.types.list_of('CloudS3IntegrationInput'), graphql_name='s3')
    ses = sgqlc.types.Field(sgqlc.types.list_of('CloudSesIntegrationInput'), graphql_name='ses')
    sns = sgqlc.types.Field(sgqlc.types.list_of('CloudSnsIntegrationInput'), graphql_name='sns')
    sqs = sgqlc.types.Field(sgqlc.types.list_of('CloudSqsIntegrationInput'), graphql_name='sqs')
    vpc = sgqlc.types.Field(sgqlc.types.list_of('CloudVpcIntegrationInput'), graphql_name='vpc')


class CloudAwsLinkAccountInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    arn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='arn')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CloudAzureAppserviceIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')


class CloudAzureCosmosdbIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')


class CloudAzureDisableIntegrationsInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    azure_appservice = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='azureAppservice')
    azure_cosmosdb = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='azureCosmosdb')
    azure_functions = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='azureFunctions')
    azure_loadbalancer = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='azureLoadbalancer')
    azure_mariadb = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='azureMariadb')
    azure_mysql = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='azureMysql')
    azure_postgresql = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='azurePostgresql')
    azure_rediscache = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='azureRediscache')
    azure_servicebus = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='azureServicebus')
    azure_sql = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='azureSql')
    azure_storage = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='azureStorage')
    azure_virtualnetworks = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='azureVirtualnetworks')
    azure_vms = sgqlc.types.Field(sgqlc.types.list_of('CloudDisableAccountIntegrationInput'), graphql_name='azureVms')


class CloudAzureFunctionsIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')


class CloudAzureIntegrationsInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    azure_appservice = sgqlc.types.Field(sgqlc.types.list_of(CloudAzureAppserviceIntegrationInput), graphql_name='azureAppservice')
    azure_cosmosdb = sgqlc.types.Field(sgqlc.types.list_of(CloudAzureCosmosdbIntegrationInput), graphql_name='azureCosmosdb')
    azure_functions = sgqlc.types.Field(sgqlc.types.list_of(CloudAzureFunctionsIntegrationInput), graphql_name='azureFunctions')
    azure_loadbalancer = sgqlc.types.Field(sgqlc.types.list_of('CloudAzureLoadbalancerIntegrationInput'), graphql_name='azureLoadbalancer')
    azure_mariadb = sgqlc.types.Field(sgqlc.types.list_of('CloudAzureMariadbIntegrationInput'), graphql_name='azureMariadb')
    azure_mysql = sgqlc.types.Field(sgqlc.types.list_of('CloudAzureMysqlIntegrationInput'), graphql_name='azureMysql')
    azure_postgresql = sgqlc.types.Field(sgqlc.types.list_of('CloudAzurePostgresqlIntegrationInput'), graphql_name='azurePostgresql')
    azure_rediscache = sgqlc.types.Field(sgqlc.types.list_of('CloudAzureRediscacheIntegrationInput'), graphql_name='azureRediscache')
    azure_servicebus = sgqlc.types.Field(sgqlc.types.list_of('CloudAzureServicebusIntegrationInput'), graphql_name='azureServicebus')
    azure_sql = sgqlc.types.Field(sgqlc.types.list_of('CloudAzureSqlIntegrationInput'), graphql_name='azureSql')
    azure_storage = sgqlc.types.Field(sgqlc.types.list_of('CloudAzureStorageIntegrationInput'), graphql_name='azureStorage')
    azure_virtualnetworks = sgqlc.types.Field(sgqlc.types.list_of('CloudAzureVirtualnetworksIntegrationInput'), graphql_name='azureVirtualnetworks')
    azure_vms = sgqlc.types.Field(sgqlc.types.list_of('CloudAzureVmsIntegrationInput'), graphql_name='azureVms')


class CloudAzureLinkAccountInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    application_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='applicationId')
    client_secret = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientSecret')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    subscription_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='subscriptionId')
    tenant_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tenantId')


class CloudAzureLoadbalancerIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')


class CloudAzureMariadbIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')


class CloudAzureMysqlIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')


class CloudAzurePostgresqlIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')


class CloudAzureRediscacheIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')


class CloudAzureServicebusIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')


class CloudAzureSqlIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')


class CloudAzureStorageIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')


class CloudAzureVirtualnetworksIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')


class CloudAzureVmsIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')


class CloudBillingIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudCloudfrontIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    fetch_lambdas_at_edge = sgqlc.types.Field(Boolean, graphql_name='fetchLambdasAtEdge')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudCloudtrailIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudDisableAccountIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')


class CloudDisableIntegrationsInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws = sgqlc.types.Field(CloudAwsDisableIntegrationsInput, graphql_name='aws')
    azure = sgqlc.types.Field(CloudAzureDisableIntegrationsInput, graphql_name='azure')
    gcp = sgqlc.types.Field('CloudGcpDisableIntegrationsInput', graphql_name='gcp')


class CloudDynamodbIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudEbsIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudEc2IntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_ip_addresses = sgqlc.types.Field(Boolean, graphql_name='fetchIpAddresses')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudEcsIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudEfsIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudElasticacheIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudElasticbeanstalkIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudElasticsearchIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_nodes = sgqlc.types.Field(Boolean, graphql_name='fetchNodes')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudElbIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudEmrIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudGcpAppengineIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudGcpBigqueryIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudGcpDisableIntegrationsInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    gcp_appengine = sgqlc.types.Field(sgqlc.types.list_of(CloudDisableAccountIntegrationInput), graphql_name='gcpAppengine')
    gcp_bigquery = sgqlc.types.Field(sgqlc.types.list_of(CloudDisableAccountIntegrationInput), graphql_name='gcpBigquery')
    gcp_functions = sgqlc.types.Field(sgqlc.types.list_of(CloudDisableAccountIntegrationInput), graphql_name='gcpFunctions')
    gcp_kubernetes = sgqlc.types.Field(sgqlc.types.list_of(CloudDisableAccountIntegrationInput), graphql_name='gcpKubernetes')
    gcp_loadbalancing = sgqlc.types.Field(sgqlc.types.list_of(CloudDisableAccountIntegrationInput), graphql_name='gcpLoadbalancing')
    gcp_pubsub = sgqlc.types.Field(sgqlc.types.list_of(CloudDisableAccountIntegrationInput), graphql_name='gcpPubsub')
    gcp_spanner = sgqlc.types.Field(sgqlc.types.list_of(CloudDisableAccountIntegrationInput), graphql_name='gcpSpanner')
    gcp_sql = sgqlc.types.Field(sgqlc.types.list_of(CloudDisableAccountIntegrationInput), graphql_name='gcpSql')
    gcp_storage = sgqlc.types.Field(sgqlc.types.list_of(CloudDisableAccountIntegrationInput), graphql_name='gcpStorage')
    gcp_vms = sgqlc.types.Field(sgqlc.types.list_of(CloudDisableAccountIntegrationInput), graphql_name='gcpVms')


class CloudGcpFunctionsIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudGcpIntegrationsInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    gcp_appengine = sgqlc.types.Field(sgqlc.types.list_of(CloudGcpAppengineIntegrationInput), graphql_name='gcpAppengine')
    gcp_bigquery = sgqlc.types.Field(sgqlc.types.list_of(CloudGcpBigqueryIntegrationInput), graphql_name='gcpBigquery')
    gcp_functions = sgqlc.types.Field(sgqlc.types.list_of(CloudGcpFunctionsIntegrationInput), graphql_name='gcpFunctions')
    gcp_kubernetes = sgqlc.types.Field(sgqlc.types.list_of('CloudGcpKubernetesIntegrationInput'), graphql_name='gcpKubernetes')
    gcp_loadbalancing = sgqlc.types.Field(sgqlc.types.list_of('CloudGcpLoadbalancingIntegrationInput'), graphql_name='gcpLoadbalancing')
    gcp_pubsub = sgqlc.types.Field(sgqlc.types.list_of('CloudGcpPubsubIntegrationInput'), graphql_name='gcpPubsub')
    gcp_spanner = sgqlc.types.Field(sgqlc.types.list_of('CloudGcpSpannerIntegrationInput'), graphql_name='gcpSpanner')
    gcp_sql = sgqlc.types.Field(sgqlc.types.list_of('CloudGcpSqlIntegrationInput'), graphql_name='gcpSql')
    gcp_storage = sgqlc.types.Field(sgqlc.types.list_of('CloudGcpStorageIntegrationInput'), graphql_name='gcpStorage')
    gcp_vms = sgqlc.types.Field(sgqlc.types.list_of('CloudGcpVmsIntegrationInput'), graphql_name='gcpVms')


class CloudGcpKubernetesIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudGcpLinkAccountInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectId')


class CloudGcpLoadbalancingIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudGcpPubsubIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudGcpSpannerIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudGcpSqlIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudGcpStorageIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudGcpVmsIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudHealthIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudIamIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudIntegrationsInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws = sgqlc.types.Field(CloudAwsIntegrationsInput, graphql_name='aws')
    azure = sgqlc.types.Field(CloudAzureIntegrationsInput, graphql_name='azure')
    gcp = sgqlc.types.Field(CloudGcpIntegrationsInput, graphql_name='gcp')


class CloudIotIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudKinesisFirehoseIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudKinesisIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_shards = sgqlc.types.Field(Boolean, graphql_name='fetchShards')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudLambdaIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudLinkCloudAccountsInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CloudAwsLinkAccountInput)), graphql_name='aws')
    azure = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CloudAzureLinkAccountInput)), graphql_name='azure')
    gcp = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CloudGcpLinkAccountInput)), graphql_name='gcp')


class CloudRdsIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudRedshiftIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudRenameAccountsInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CloudRoute53IntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudS3IntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudSesIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudSnsIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')


class CloudSqsIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    queue_prefixes = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='queuePrefixes')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class CloudUnlinkAccountsInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')


class CloudVpcIntegrationInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    fetch_nat_gateway = sgqlc.types.Field(Boolean, graphql_name='fetchNatGateway')
    fetch_vpn = sgqlc.types.Field(Boolean, graphql_name='fetchVpn')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkedAccountId')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')


class EntityRelationshipFilter(sgqlc.types.Input):
    __schema__ = newrelic_schema
    entity_type = sgqlc.types.Field(sgqlc.types.list_of(EntityType), graphql_name='entityType')
    infrastructure_integration_type = sgqlc.types.Field(sgqlc.types.list_of(EntityInfrastructureIntegrationType), graphql_name='infrastructureIntegrationType')


class EntitySearchQueryBuilder(sgqlc.types.Input):
    __schema__ = newrelic_schema
    alert_severity = sgqlc.types.Field(EntityAlertSeverity, graphql_name='alertSeverity')
    domain = sgqlc.types.Field(EntitySearchQueryBuilderDomain, graphql_name='domain')
    infrastructure_integration_type = sgqlc.types.Field(EntityInfrastructureIntegrationType, graphql_name='infrastructureIntegrationType')
    name = sgqlc.types.Field(String, graphql_name='name')
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of('EntitySearchQueryBuilderTag'), graphql_name='tags')
    type = sgqlc.types.Field(EntitySearchQueryBuilderType, graphql_name='type')


class EntitySearchQueryBuilderTag(sgqlc.types.Input):
    __schema__ = newrelic_schema
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class NerdStorageScopeInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(NerdStorageScope), graphql_name='name')


class TaggingTagInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    values = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='values')


class TaggingTagValueInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class TimeWindowInput(sgqlc.types.Input):
    __schema__ = newrelic_schema
    end_time = sgqlc.types.Field(sgqlc.types.non_null(EpochMilliseconds), graphql_name='endTime')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(EpochMilliseconds), graphql_name='startTime')



########################################################################
# Output Objects and Interfaces
########################################################################
class Account(sgqlc.types.Type):
    __schema__ = newrelic_schema
    cloud = sgqlc.types.Field('CloudAccountFields', graphql_name='cloud')
    id = sgqlc.types.Field(Int, graphql_name='id')
    license_key = sgqlc.types.Field(String, graphql_name='licenseKey')
    name = sgqlc.types.Field(String, graphql_name='name')
    nerd_storage = sgqlc.types.Field('NerdStorageAccountScope', graphql_name='nerdStorage')
    nrql = sgqlc.types.Field('NrdbResultContainer', graphql_name='nrql', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(Nrql), graphql_name='query', default=None)),
        ('timeout', sgqlc.types.Arg(Seconds, graphql_name='timeout', default=None)),
))
    )


class AccountOutline(sgqlc.types.Type):
    __schema__ = newrelic_schema
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    reporting_event_types = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='reportingEventTypes', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='filter', default=None)),
        ('time_window', sgqlc.types.Arg(TimeWindowInput, graphql_name='timeWindow', default=None)),
))
    )


class AccountReference(sgqlc.types.Type):
    __schema__ = newrelic_schema
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class Actor(sgqlc.types.Type):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(Account, graphql_name='account', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    accounts = sgqlc.types.Field(sgqlc.types.list_of(AccountOutline), graphql_name='accounts')
    cloud = sgqlc.types.Field('CloudActorFields', graphql_name='cloud')
    distributed_tracing = sgqlc.types.Field('DistributedTracingActorStitchedFields', graphql_name='distributedTracing')
    entities = sgqlc.types.Field(sgqlc.types.list_of('Entity'), graphql_name='entities', args=sgqlc.types.ArgDict((
        ('guids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(EntityGuid)), graphql_name='guids', default=None)),
))
    )
    entity = sgqlc.types.Field('Entity', graphql_name='entity', args=sgqlc.types.ArgDict((
        ('guid', sgqlc.types.Arg(sgqlc.types.non_null(EntityGuid), graphql_name='guid', default=None)),
))
    )
    entity_search = sgqlc.types.Field('EntitySearch', graphql_name='entitySearch', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('query_builder', sgqlc.types.Arg(EntitySearchQueryBuilder, graphql_name='queryBuilder', default=None)),
        ('sort_by', sgqlc.types.Arg(sgqlc.types.list_of(EntitySearchSortCriteria), graphql_name='sortBy', default=['NAME'])),
))
    )
    nerd_storage = sgqlc.types.Field('NerdStorageActorScope', graphql_name='nerdStorage')
    user = sgqlc.types.Field('User', graphql_name='user')


class AgentRelease(sgqlc.types.Type):
    __schema__ = newrelic_schema
    date = sgqlc.types.Field(Date, graphql_name='date')
    version = sgqlc.types.Field(String, graphql_name='version')


class AlertableEntity(sgqlc.types.Interface):
    __schema__ = newrelic_schema
    alert_severity = sgqlc.types.Field(EntityAlertSeverity, graphql_name='alertSeverity')
    alert_violations = sgqlc.types.Field(sgqlc.types.list_of('EntityAlertViolation'), graphql_name='alertViolations', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(sgqlc.types.non_null(EpochMilliseconds), graphql_name='endTime', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(EpochMilliseconds), graphql_name='startTime', default=None)),
))
    )
    recent_alert_violations = sgqlc.types.Field(sgqlc.types.list_of('EntityAlertViolation'), graphql_name='recentAlertViolations', args=sgqlc.types.ArgDict((
        ('count', sgqlc.types.Arg(Int, graphql_name='count', default=10)),
))
    )


class AlertableEntityOutline(sgqlc.types.Interface):
    __schema__ = newrelic_schema
    alert_severity = sgqlc.types.Field(EntityAlertSeverity, graphql_name='alertSeverity')


class AlertsMutingRuleCondition(sgqlc.types.Type):
    __schema__ = newrelic_schema
    attribute = sgqlc.types.Field(sgqlc.types.non_null(AlertsMutingRuleConditionAttribute), graphql_name='attribute')
    attribute_param = sgqlc.types.Field(String, graphql_name='attributeParam')
    operator = sgqlc.types.Field(sgqlc.types.non_null(AlertsMutingRuleConditionOperator), graphql_name='operator')
    values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='values')


class AlertsMutingRuleConditionGroup(sgqlc.types.Type):
    __schema__ = newrelic_schema
    conditions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AlertsMutingRuleCondition))), graphql_name='conditions')
    operator = sgqlc.types.Field(sgqlc.types.non_null(AlertsMutingRuleConditionGroupOperator), graphql_name='operator')


class ApmApplicationDeployment(sgqlc.types.Type):
    __schema__ = newrelic_schema
    changelog = sgqlc.types.Field(String, graphql_name='changelog')
    description = sgqlc.types.Field(String, graphql_name='description')
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    revision = sgqlc.types.Field(String, graphql_name='revision')
    timestamp = sgqlc.types.Field(EpochMilliseconds, graphql_name='timestamp')
    user = sgqlc.types.Field(String, graphql_name='user')


class ApmApplicationRunningAgentVersions(sgqlc.types.Type):
    __schema__ = newrelic_schema
    max_version = sgqlc.types.Field(String, graphql_name='maxVersion')
    min_version = sgqlc.types.Field(String, graphql_name='minVersion')


class ApmApplicationSettings(sgqlc.types.Type):
    __schema__ = newrelic_schema
    apdex_target = sgqlc.types.Field(Float, graphql_name='apdexTarget')
    server_side_config = sgqlc.types.Field(Boolean, graphql_name='serverSideConfig')


class ApmApplicationSummaryData(sgqlc.types.Type):
    __schema__ = newrelic_schema
    apdex_score = sgqlc.types.Field(Float, graphql_name='apdexScore')
    error_rate = sgqlc.types.Field(Float, graphql_name='errorRate')
    host_count = sgqlc.types.Field(Int, graphql_name='hostCount')
    instance_count = sgqlc.types.Field(Int, graphql_name='instanceCount')
    non_web_response_time_average = sgqlc.types.Field(Seconds, graphql_name='nonWebResponseTimeAverage')
    non_web_throughput = sgqlc.types.Field(Float, graphql_name='nonWebThroughput')
    response_time_average = sgqlc.types.Field(Seconds, graphql_name='responseTimeAverage')
    throughput = sgqlc.types.Field(Float, graphql_name='throughput')
    web_response_time_average = sgqlc.types.Field(Seconds, graphql_name='webResponseTimeAverage')
    web_throughput = sgqlc.types.Field(Float, graphql_name='webThroughput')


class ApmExternalServiceSummaryData(sgqlc.types.Type):
    __schema__ = newrelic_schema
    response_time_average = sgqlc.types.Field(Float, graphql_name='responseTimeAverage')
    throughput = sgqlc.types.Field(Float, graphql_name='throughput')


class BrowserApplicationRunningAgentVersions(sgqlc.types.Type):
    __schema__ = newrelic_schema
    max_version = sgqlc.types.Field(Int, graphql_name='maxVersion')
    min_version = sgqlc.types.Field(Int, graphql_name='minVersion')


class BrowserApplicationSettings(sgqlc.types.Type):
    __schema__ = newrelic_schema
    apdex_target = sgqlc.types.Field(Float, graphql_name='apdexTarget')


class BrowserApplicationSummaryData(sgqlc.types.Type):
    __schema__ = newrelic_schema
    ajax_request_throughput = sgqlc.types.Field(Float, graphql_name='ajaxRequestThroughput')
    ajax_response_time_average = sgqlc.types.Field(Float, graphql_name='ajaxResponseTimeAverage')
    js_error_rate = sgqlc.types.Field(Float, graphql_name='jsErrorRate')
    page_load_throughput = sgqlc.types.Field(Float, graphql_name='pageLoadThroughput')
    page_load_time_average = sgqlc.types.Field(Float, graphql_name='pageLoadTimeAverage')
    page_load_time_median = sgqlc.types.Field(Float, graphql_name='pageLoadTimeMedian')
    spa_response_time_average = sgqlc.types.Field(Float, graphql_name='spaResponseTimeAverage')
    spa_response_time_median = sgqlc.types.Field(Float, graphql_name='spaResponseTimeMedian')


class CloudAccountFields(sgqlc.types.Type):
    __schema__ = newrelic_schema
    linked_account = sgqlc.types.Field('CloudLinkedAccount', graphql_name='linkedAccount', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
))
    )
    linked_accounts = sgqlc.types.Field(sgqlc.types.list_of('CloudLinkedAccount'), graphql_name='linkedAccounts')
    provider = sgqlc.types.Field('CloudProvider', graphql_name='provider', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(String, graphql_name='slug', default=None)),
))
    )
    providers = sgqlc.types.Field(sgqlc.types.list_of('CloudProvider'), graphql_name='providers')


class CloudAccountMutationError(sgqlc.types.Type):
    __schema__ = newrelic_schema
    linked_account_id = sgqlc.types.Field(Int, graphql_name='linkedAccountId')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    provider_slug = sgqlc.types.Field(String, graphql_name='providerSlug')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')


class CloudActorFields(sgqlc.types.Type):
    __schema__ = newrelic_schema
    linked_accounts = sgqlc.types.Field(sgqlc.types.list_of('CloudLinkedAccount'), graphql_name='linkedAccounts', args=sgqlc.types.ArgDict((
        ('provider', sgqlc.types.Arg(String, graphql_name='provider', default=None)),
))
    )


class CloudConfigureIntegrationPayload(sgqlc.types.Type):
    __schema__ = newrelic_schema
    errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CloudIntegrationMutationError'))), graphql_name='errors')
    integrations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CloudIntegration'))), graphql_name='integrations')


class CloudDisableIntegrationPayload(sgqlc.types.Type):
    __schema__ = newrelic_schema
    disabled_integrations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CloudIntegration'))), graphql_name='disabledIntegrations')
    errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CloudIntegrationMutationError'))), graphql_name='errors')


class CloudIntegration(sgqlc.types.Interface):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    linked_account = sgqlc.types.Field('CloudLinkedAccount', graphql_name='linkedAccount')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field('CloudService', graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudIntegrationMutationError(sgqlc.types.Type):
    __schema__ = newrelic_schema
    integration_slug = sgqlc.types.Field(String, graphql_name='integrationSlug')
    linked_account_id = sgqlc.types.Field(Int, graphql_name='linkedAccountId')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')


class CloudLinkAccountPayload(sgqlc.types.Type):
    __schema__ = newrelic_schema
    errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CloudAccountMutationError))), graphql_name='errors')
    linked_accounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CloudLinkedAccount'))), graphql_name='linkedAccounts')


class CloudLinkedAccount(sgqlc.types.Type):
    __schema__ = newrelic_schema
    auth_label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='authLabel')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    disabled = sgqlc.types.Field(Boolean, graphql_name='disabled')
    external_id = sgqlc.types.Field(String, graphql_name='externalId')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    integration = sgqlc.types.Field(sgqlc.types.non_null(CloudIntegration), graphql_name='integration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    integrations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CloudIntegration))), graphql_name='integrations', args=sgqlc.types.ArgDict((
        ('service', sgqlc.types.Arg(String, graphql_name='service', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    provider = sgqlc.types.Field(sgqlc.types.non_null('CloudProvider'), graphql_name='provider')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudProvider(sgqlc.types.Interface):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    icon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='icon')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    service = sgqlc.types.Field('CloudService', graphql_name='service', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
))
    )
    services = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CloudService'))), graphql_name='services')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudRenameAccountPayload(sgqlc.types.Type):
    __schema__ = newrelic_schema
    errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CloudAccountMutationError))), graphql_name='errors')
    linked_accounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CloudLinkedAccount))), graphql_name='linkedAccounts')


class CloudService(sgqlc.types.Type):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    icon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='icon')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEnabled')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    provider = sgqlc.types.Field(sgqlc.types.non_null(CloudProvider), graphql_name='provider')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudUnlinkAccountPayload(sgqlc.types.Type):
    __schema__ = newrelic_schema
    errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CloudAccountMutationError))), graphql_name='errors')
    unlinked_accounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CloudLinkedAccount))), graphql_name='unlinkedAccounts')


class DistributedTracingActorStitchedFields(sgqlc.types.Type):
    __schema__ = newrelic_schema
    trace = sgqlc.types.Field('DistributedTracingTrace', graphql_name='trace', args=sgqlc.types.ArgDict((
        ('timestamp', sgqlc.types.Arg(EpochMilliseconds, graphql_name='timestamp', default=None)),
        ('trace_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='traceId', default=None)),
))
    )


class DistributedTracingSpan(sgqlc.types.Type):
    __schema__ = newrelic_schema
    attributes = sgqlc.types.Field(DistributedTracingSpanAttributes, graphql_name='attributes')
    client_type = sgqlc.types.Field(DistributedTracingSpanClientType, graphql_name='clientType')
    duration_ms = sgqlc.types.Field(Milliseconds, graphql_name='durationMs')
    entity_guid = sgqlc.types.Field(String, graphql_name='entityGuid')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    parent_id = sgqlc.types.Field(String, graphql_name='parentId')
    process_boundary = sgqlc.types.Field(sgqlc.types.non_null(DistributedTracingSpanProcessBoundary), graphql_name='processBoundary')
    span_anomalies = sgqlc.types.Field(sgqlc.types.list_of('DistributedTracingSpanAnomaly'), graphql_name='spanAnomalies')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(EpochMilliseconds), graphql_name='timestamp')
    trace_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='traceId')


class DistributedTracingSpanAnomaly(sgqlc.types.Type):
    __schema__ = newrelic_schema
    anomalous_value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='anomalousValue')
    anomaly_type = sgqlc.types.Field(sgqlc.types.non_null(DistributedTracingSpanAnomalyType), graphql_name='anomalyType')
    average_measure = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='averageMeasure')


class DistributedTracingSpanConnection(sgqlc.types.Type):
    __schema__ = newrelic_schema
    child = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='child')
    parent = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='parent')


class DistributedTracingTrace(sgqlc.types.Type):
    __schema__ = newrelic_schema
    duration_ms = sgqlc.types.Field(Milliseconds, graphql_name='durationMs')
    entities = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EntityOutline'))), graphql_name='entities')
    entity_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='entityCount')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    span_connections = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(DistributedTracingSpanConnection)), graphql_name='spanConnections')
    spans = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DistributedTracingSpan))), graphql_name='spans')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(EpochMilliseconds), graphql_name='timestamp')


class DocumentationFields(sgqlc.types.Type):
    __schema__ = newrelic_schema
    agent_releases = sgqlc.types.Field(sgqlc.types.list_of(AgentRelease), graphql_name='agentReleases', args=sgqlc.types.ArgDict((
        ('agent_name', sgqlc.types.Arg(sgqlc.types.non_null(AgentReleasesFilter), graphql_name='agentName', default=None)),
))
    )


class Entity(sgqlc.types.Interface):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    nerd_storage = sgqlc.types.Field('NerdStorageEntityScope', graphql_name='nerdStorage')
    nrdb_query = sgqlc.types.Field('NrdbResultContainer', graphql_name='nrdbQuery', args=sgqlc.types.ArgDict((
        ('nrql', sgqlc.types.Arg(sgqlc.types.non_null(Nrql), graphql_name='nrql', default=None)),
        ('timeout', sgqlc.types.Arg(Seconds, graphql_name='timeout', default=None)),
))
    )
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    relationships = sgqlc.types.Field(sgqlc.types.list_of('EntityRelationship'), graphql_name='relationships', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(EpochMilliseconds, graphql_name='endTime', default=None)),
        ('filter', sgqlc.types.Arg(EntityRelationshipFilter, graphql_name='filter', default=None)),
))
    )
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of('EntityTag'), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class EntityAlertViolation(sgqlc.types.Type):
    __schema__ = newrelic_schema
    agent_url = sgqlc.types.Field(String, graphql_name='agentUrl')
    alert_severity = sgqlc.types.Field(EntityAlertSeverity, graphql_name='alertSeverity')
    closed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='closedAt')
    label = sgqlc.types.Field(String, graphql_name='label')
    level = sgqlc.types.Field(String, graphql_name='level')
    opened_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='openedAt')
    violation_id = sgqlc.types.Field(Int, graphql_name='violationId')
    violation_url = sgqlc.types.Field(String, graphql_name='violationUrl')


class EntityOutline(sgqlc.types.Interface):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of('EntityTag'), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class EntityRelationship(sgqlc.types.Type):
    __schema__ = newrelic_schema
    source = sgqlc.types.Field('EntityRelationshipNode', graphql_name='source')
    target = sgqlc.types.Field('EntityRelationshipNode', graphql_name='target')
    type = sgqlc.types.Field(EntityRelationshipType, graphql_name='type')


class EntityRelationshipNode(sgqlc.types.Type):
    __schema__ = newrelic_schema
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    entity = sgqlc.types.Field(EntityOutline, graphql_name='entity')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')


class EntitySearch(sgqlc.types.Type):
    __schema__ = newrelic_schema
    count = sgqlc.types.Field(Int, graphql_name='count')
    query = sgqlc.types.Field(String, graphql_name='query')
    results = sgqlc.types.Field('EntitySearchResult', graphql_name='results', args=sgqlc.types.ArgDict((
        ('cursor', sgqlc.types.Arg(String, graphql_name='cursor', default=None)),
))
    )
    types = sgqlc.types.Field(sgqlc.types.list_of('EntitySearchTypes'), graphql_name='types')


class EntitySearchResult(sgqlc.types.Type):
    __schema__ = newrelic_schema
    entities = sgqlc.types.Field(sgqlc.types.list_of(EntityOutline), graphql_name='entities')
    next_cursor = sgqlc.types.Field(String, graphql_name='nextCursor')


class EntitySearchTypes(sgqlc.types.Type):
    __schema__ = newrelic_schema
    count = sgqlc.types.Field(Int, graphql_name='count')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    type = sgqlc.types.Field(String, graphql_name='type')


class EntityTag(sgqlc.types.Type):
    __schema__ = newrelic_schema
    key = sgqlc.types.Field(String, graphql_name='key')
    values = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='values')


class EventAttributeDefinition(sgqlc.types.Type):
    __schema__ = newrelic_schema
    category = sgqlc.types.Field(String, graphql_name='category')
    definition = sgqlc.types.Field(String, graphql_name='definition')
    documentation_url = sgqlc.types.Field(String, graphql_name='documentationUrl')
    label = sgqlc.types.Field(String, graphql_name='label')
    name = sgqlc.types.Field(String, graphql_name='name')


class EventDefinition(sgqlc.types.Type):
    __schema__ = newrelic_schema
    attributes = sgqlc.types.Field(sgqlc.types.list_of(EventAttributeDefinition), graphql_name='attributes')
    definition = sgqlc.types.Field(String, graphql_name='definition')
    label = sgqlc.types.Field(String, graphql_name='label')
    name = sgqlc.types.Field(String, graphql_name='name')


class InfrastructureHostSummaryData(sgqlc.types.Type):
    __schema__ = newrelic_schema
    cpu_utilization_percent = sgqlc.types.Field(Float, graphql_name='cpuUtilizationPercent')
    disk_used_percent = sgqlc.types.Field(Float, graphql_name='diskUsedPercent')
    memory_used_percent = sgqlc.types.Field(Float, graphql_name='memoryUsedPercent')
    network_receive_rate = sgqlc.types.Field(Float, graphql_name='networkReceiveRate')
    network_transmit_rate = sgqlc.types.Field(Float, graphql_name='networkTransmitRate')
    services_count = sgqlc.types.Field(Int, graphql_name='servicesCount')


class InfrastructureIntegrationEntity(sgqlc.types.Interface):
    __schema__ = newrelic_schema
    integration_type_code = sgqlc.types.Field(String, graphql_name='integrationTypeCode')


class InfrastructureIntegrationEntityOutline(sgqlc.types.Interface):
    __schema__ = newrelic_schema
    integration_type_code = sgqlc.types.Field(String, graphql_name='integrationTypeCode')


class MobileAppSummaryData(sgqlc.types.Type):
    __schema__ = newrelic_schema
    app_launch_count = sgqlc.types.Field(Int, graphql_name='appLaunchCount')
    crash_count = sgqlc.types.Field(Int, graphql_name='crashCount')
    crash_rate = sgqlc.types.Field(Float, graphql_name='crashRate')
    http_error_rate = sgqlc.types.Field(Float, graphql_name='httpErrorRate')
    http_request_count = sgqlc.types.Field(Int, graphql_name='httpRequestCount')
    http_request_rate = sgqlc.types.Field(Float, graphql_name='httpRequestRate')
    http_response_time_average = sgqlc.types.Field(Float, graphql_name='httpResponseTimeAverage')
    mobile_session_count = sgqlc.types.Field(Int, graphql_name='mobileSessionCount')
    network_failure_rate = sgqlc.types.Field(Float, graphql_name='networkFailureRate')
    users_affected_count = sgqlc.types.Field(Int, graphql_name='usersAffectedCount')


class NerdStorageAccountScope(sgqlc.types.Type):
    __schema__ = newrelic_schema
    collection = sgqlc.types.Field(sgqlc.types.list_of('NerdStorageCollectionMember'), graphql_name='collection', args=sgqlc.types.ArgDict((
        ('collection', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='collection', default=None)),
))
    )
    document = sgqlc.types.Field(NerdStorageDocument, graphql_name='document', args=sgqlc.types.ArgDict((
        ('collection', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='collection', default=None)),
        ('document_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='documentId', default=None)),
))
    )


class NerdStorageActorScope(sgqlc.types.Type):
    __schema__ = newrelic_schema
    collection = sgqlc.types.Field(sgqlc.types.list_of('NerdStorageCollectionMember'), graphql_name='collection', args=sgqlc.types.ArgDict((
        ('collection', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='collection', default=None)),
))
    )
    document = sgqlc.types.Field(NerdStorageDocument, graphql_name='document', args=sgqlc.types.ArgDict((
        ('collection', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='collection', default=None)),
        ('document_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='documentId', default=None)),
))
    )


class NerdStorageCollectionMember(sgqlc.types.Type):
    __schema__ = newrelic_schema
    document = sgqlc.types.Field(NerdStorageDocument, graphql_name='document')
    id = sgqlc.types.Field(String, graphql_name='id')


class NerdStorageDeleteResult(sgqlc.types.Type):
    __schema__ = newrelic_schema
    deleted = sgqlc.types.Field(Int, graphql_name='deleted')


class NerdStorageEntityScope(sgqlc.types.Type):
    __schema__ = newrelic_schema
    collection = sgqlc.types.Field(sgqlc.types.list_of(NerdStorageCollectionMember), graphql_name='collection', args=sgqlc.types.ArgDict((
        ('collection', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='collection', default=None)),
))
    )
    document = sgqlc.types.Field(NerdStorageDocument, graphql_name='document', args=sgqlc.types.ArgDict((
        ('collection', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='collection', default=None)),
        ('document_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='documentId', default=None)),
))
    )


class NrdbMetadata(sgqlc.types.Type):
    __schema__ = newrelic_schema
    event_types = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='eventTypes')
    messages = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='messages')
    time_window = sgqlc.types.Field('NrdbMetadataTimeWindow', graphql_name='timeWindow')


class NrdbMetadataTimeWindow(sgqlc.types.Type):
    __schema__ = newrelic_schema
    begin = sgqlc.types.Field(EpochMilliseconds, graphql_name='begin')
    compare_with = sgqlc.types.Field(String, graphql_name='compareWith')
    end = sgqlc.types.Field(EpochMilliseconds, graphql_name='end')
    since = sgqlc.types.Field(String, graphql_name='since')
    until = sgqlc.types.Field(String, graphql_name='until')


class NrdbResultContainer(sgqlc.types.Type):
    __schema__ = newrelic_schema
    current_results = sgqlc.types.Field(sgqlc.types.list_of(NrdbResult), graphql_name='currentResults')
    embedded_chart_url = sgqlc.types.Field(String, graphql_name='embeddedChartUrl', args=sgqlc.types.ArgDict((
        ('chart_type', sgqlc.types.Arg(EmbeddedChartType, graphql_name='chartType', default=None)),
))
    )
    event_definitions = sgqlc.types.Field(sgqlc.types.list_of(EventDefinition), graphql_name='eventDefinitions')
    metadata = sgqlc.types.Field(NrdbMetadata, graphql_name='metadata')
    nrql = sgqlc.types.Field(Nrql, graphql_name='nrql')
    other_result = sgqlc.types.Field(NrdbResult, graphql_name='otherResult')
    previous_results = sgqlc.types.Field(sgqlc.types.list_of(NrdbResult), graphql_name='previousResults')
    results = sgqlc.types.Field(sgqlc.types.list_of(NrdbResult), graphql_name='results')
    static_chart_url = sgqlc.types.Field(String, graphql_name='staticChartUrl', args=sgqlc.types.ArgDict((
        ('chart_type', sgqlc.types.Arg(ChartImageType, graphql_name='chartType', default=None)),
        ('format', sgqlc.types.Arg(ChartFormatType, graphql_name='format', default='PNG')),
        ('height', sgqlc.types.Arg(Int, graphql_name='height', default=None)),
        ('width', sgqlc.types.Arg(Int, graphql_name='width', default=None)),
))
    )
    suggested_facets = sgqlc.types.Field(sgqlc.types.list_of('NrqlFacetSuggestion'), graphql_name='suggestedFacets')
    suggested_queries = sgqlc.types.Field('SuggestedNrqlQueryResponse', graphql_name='suggestedQueries', args=sgqlc.types.ArgDict((
        ('anomaly_time_window', sgqlc.types.Arg(TimeWindowInput, graphql_name='anomalyTimeWindow', default=None)),
))
    )
    total_result = sgqlc.types.Field(NrdbResult, graphql_name='totalResult')


class NrqlFacetSuggestion(sgqlc.types.Type):
    __schema__ = newrelic_schema
    attributes = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='attributes')
    nrql = sgqlc.types.Field(Nrql, graphql_name='nrql')


class RequestContext(sgqlc.types.Type):
    __schema__ = newrelic_schema
    api_key = sgqlc.types.Field(String, graphql_name='apiKey')
    user_id = sgqlc.types.Field(ID, graphql_name='userId')


class RootMutationType(sgqlc.types.Type):
    __schema__ = newrelic_schema
    cloud_configure_integration = sgqlc.types.Field(CloudConfigureIntegrationPayload, graphql_name='cloudConfigureIntegration', args=sgqlc.types.ArgDict((
        ('account_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='accountId', default=None)),
        ('integrations', sgqlc.types.Arg(sgqlc.types.non_null(CloudIntegrationsInput), graphql_name='integrations', default=None)),
))
    )
    cloud_disable_integration = sgqlc.types.Field(CloudDisableIntegrationPayload, graphql_name='cloudDisableIntegration', args=sgqlc.types.ArgDict((
        ('account_id', sgqlc.types.Arg(Int, graphql_name='accountId', default=None)),
        ('integrations', sgqlc.types.Arg(CloudDisableIntegrationsInput, graphql_name='integrations', default=None)),
))
    )
    cloud_link_account = sgqlc.types.Field(CloudLinkAccountPayload, graphql_name='cloudLinkAccount', args=sgqlc.types.ArgDict((
        ('account_id', sgqlc.types.Arg(Int, graphql_name='accountId', default=None)),
        ('accounts', sgqlc.types.Arg(CloudLinkCloudAccountsInput, graphql_name='accounts', default=None)),
))
    )
    cloud_rename_account = sgqlc.types.Field(CloudRenameAccountPayload, graphql_name='cloudRenameAccount', args=sgqlc.types.ArgDict((
        ('account_id', sgqlc.types.Arg(Int, graphql_name='accountId', default=None)),
        ('accounts', sgqlc.types.Arg(sgqlc.types.list_of(CloudRenameAccountsInput), graphql_name='accounts', default=None)),
))
    )
    cloud_unlink_account = sgqlc.types.Field(CloudUnlinkAccountPayload, graphql_name='cloudUnlinkAccount', args=sgqlc.types.ArgDict((
        ('account_id', sgqlc.types.Arg(Int, graphql_name='accountId', default=None)),
        ('accounts', sgqlc.types.Arg(sgqlc.types.list_of(CloudUnlinkAccountsInput), graphql_name='accounts', default=None)),
))
    )
    nerd_storage_delete_collection = sgqlc.types.Field(NerdStorageDeleteResult, graphql_name='nerdStorageDeleteCollection', args=sgqlc.types.ArgDict((
        ('collection', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='collection', default=None)),
        ('scope', sgqlc.types.Arg(sgqlc.types.non_null(NerdStorageScopeInput), graphql_name='scope', default=None)),
))
    )
    nerd_storage_delete_document = sgqlc.types.Field(NerdStorageDeleteResult, graphql_name='nerdStorageDeleteDocument', args=sgqlc.types.ArgDict((
        ('collection', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='collection', default=None)),
        ('document_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='documentId', default=None)),
        ('scope', sgqlc.types.Arg(sgqlc.types.non_null(NerdStorageScopeInput), graphql_name='scope', default=None)),
))
    )
    nerd_storage_write_document = sgqlc.types.Field(NerdStorageDocument, graphql_name='nerdStorageWriteDocument', args=sgqlc.types.ArgDict((
        ('collection', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='collection', default=None)),
        ('document', sgqlc.types.Arg(sgqlc.types.non_null(NerdStorageDocument), graphql_name='document', default=None)),
        ('document_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='documentId', default=None)),
        ('scope', sgqlc.types.Arg(sgqlc.types.non_null(NerdStorageScopeInput), graphql_name='scope', default=None)),
))
    )
    tagging_add_tags_to_entity = sgqlc.types.Field('TaggingMutationResult', graphql_name='taggingAddTagsToEntity', args=sgqlc.types.ArgDict((
        ('guid', sgqlc.types.Arg(sgqlc.types.non_null(EntityGuid), graphql_name='guid', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TaggingTagInput))), graphql_name='tags', default=None)),
))
    )
    tagging_delete_tag_from_entity = sgqlc.types.Field('TaggingMutationResult', graphql_name='taggingDeleteTagFromEntity', args=sgqlc.types.ArgDict((
        ('guid', sgqlc.types.Arg(sgqlc.types.non_null(EntityGuid), graphql_name='guid', default=None)),
        ('tag_keys', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tagKeys', default=None)),
))
    )
    tagging_delete_tag_values_from_entity = sgqlc.types.Field('TaggingMutationResult', graphql_name='taggingDeleteTagValuesFromEntity', args=sgqlc.types.ArgDict((
        ('guid', sgqlc.types.Arg(sgqlc.types.non_null(EntityGuid), graphql_name='guid', default=None)),
        ('tag_values', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TaggingTagValueInput))), graphql_name='tagValues', default=None)),
))
    )
    tagging_replace_tags_on_entity = sgqlc.types.Field('TaggingMutationResult', graphql_name='taggingReplaceTagsOnEntity', args=sgqlc.types.ArgDict((
        ('guid', sgqlc.types.Arg(sgqlc.types.non_null(EntityGuid), graphql_name='guid', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TaggingTagInput))), graphql_name='tags', default=None)),
))
    )


class RootQueryType(sgqlc.types.Type):
    __schema__ = newrelic_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    docs = sgqlc.types.Field(DocumentationFields, graphql_name='docs')
    request_context = sgqlc.types.Field(RequestContext, graphql_name='requestContext')


class SuggestedNrqlQuery(sgqlc.types.Interface):
    __schema__ = newrelic_schema
    nrql = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nrql')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class SuggestedNrqlQueryAnomaly(sgqlc.types.Type):
    __schema__ = newrelic_schema
    time_window = sgqlc.types.Field(sgqlc.types.non_null('TimeWindow'), graphql_name='timeWindow')


class SuggestedNrqlQueryResponse(sgqlc.types.Type):
    __schema__ = newrelic_schema
    suggestions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SuggestedNrqlQuery)), graphql_name='suggestions')


class SyntheticMonitorSummaryData(sgqlc.types.Type):
    __schema__ = newrelic_schema
    locations_failing = sgqlc.types.Field(Int, graphql_name='locationsFailing')
    locations_running = sgqlc.types.Field(Int, graphql_name='locationsRunning')
    success_rate = sgqlc.types.Field(Float, graphql_name='successRate')


class TaggingMutationError(sgqlc.types.Type):
    __schema__ = newrelic_schema
    message = sgqlc.types.Field(String, graphql_name='message')
    type = sgqlc.types.Field(TaggingMutationErrorType, graphql_name='type')


class TaggingMutationResult(sgqlc.types.Type):
    __schema__ = newrelic_schema
    errors = sgqlc.types.Field(sgqlc.types.list_of(TaggingMutationError), graphql_name='errors')


class TimeWindow(sgqlc.types.Type):
    __schema__ = newrelic_schema
    end_time = sgqlc.types.Field(EpochMilliseconds, graphql_name='endTime')
    start_time = sgqlc.types.Field(EpochMilliseconds, graphql_name='startTime')


class User(sgqlc.types.Type):
    __schema__ = newrelic_schema
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UserReference(sgqlc.types.Type):
    __schema__ = newrelic_schema
    email = sgqlc.types.Field(String, graphql_name='email')
    gravatar = sgqlc.types.Field(String, graphql_name='gravatar')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class ApmApplicationEntity(sgqlc.types.Type, AlertableEntity, Entity):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    alert_severity = sgqlc.types.Field(EntityAlertSeverity, graphql_name='alertSeverity')
    alert_violations = sgqlc.types.Field(sgqlc.types.list_of(EntityAlertViolation), graphql_name='alertViolations', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(sgqlc.types.non_null(EpochMilliseconds), graphql_name='endTime', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(EpochMilliseconds), graphql_name='startTime', default=None)),
))
    )
    apm_summary = sgqlc.types.Field(ApmApplicationSummaryData, graphql_name='apmSummary')
    application_id = sgqlc.types.Field(Int, graphql_name='applicationId')
    deployments = sgqlc.types.Field(sgqlc.types.list_of(ApmApplicationDeployment), graphql_name='deployments', args=sgqlc.types.ArgDict((
        ('time_window', sgqlc.types.Arg(TimeWindowInput, graphql_name='timeWindow', default=None)),
))
    )
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    language = sgqlc.types.Field(String, graphql_name='language')
    name = sgqlc.types.Field(String, graphql_name='name')
    nerd_storage = sgqlc.types.Field(NerdStorageEntityScope, graphql_name='nerdStorage')
    nrdb_query = sgqlc.types.Field(NrdbResultContainer, graphql_name='nrdbQuery', args=sgqlc.types.ArgDict((
        ('nrql', sgqlc.types.Arg(sgqlc.types.non_null(Nrql), graphql_name='nrql', default=None)),
        ('timeout', sgqlc.types.Arg(Seconds, graphql_name='timeout', default=None)),
))
    )
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    recent_alert_violations = sgqlc.types.Field(sgqlc.types.list_of(EntityAlertViolation), graphql_name='recentAlertViolations', args=sgqlc.types.ArgDict((
        ('count', sgqlc.types.Arg(Int, graphql_name='count', default=10)),
))
    )
    relationships = sgqlc.types.Field(sgqlc.types.list_of(EntityRelationship), graphql_name='relationships', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(EpochMilliseconds, graphql_name='endTime', default=None)),
        ('filter', sgqlc.types.Arg(EntityRelationshipFilter, graphql_name='filter', default=None)),
))
    )
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    running_agent_versions = sgqlc.types.Field(ApmApplicationRunningAgentVersions, graphql_name='runningAgentVersions')
    settings = sgqlc.types.Field(ApmApplicationSettings, graphql_name='settings')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class ApmApplicationEntityOutline(sgqlc.types.Type, AlertableEntityOutline, EntityOutline):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    alert_severity = sgqlc.types.Field(EntityAlertSeverity, graphql_name='alertSeverity')
    apm_summary = sgqlc.types.Field(ApmApplicationSummaryData, graphql_name='apmSummary')
    application_id = sgqlc.types.Field(Int, graphql_name='applicationId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    language = sgqlc.types.Field(String, graphql_name='language')
    name = sgqlc.types.Field(String, graphql_name='name')
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    running_agent_versions = sgqlc.types.Field(ApmApplicationRunningAgentVersions, graphql_name='runningAgentVersions')
    settings = sgqlc.types.Field(ApmApplicationSettings, graphql_name='settings')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class ApmDatabaseInstanceEntity(sgqlc.types.Type, Entity):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    host = sgqlc.types.Field(String, graphql_name='host')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    nerd_storage = sgqlc.types.Field(NerdStorageEntityScope, graphql_name='nerdStorage')
    nrdb_query = sgqlc.types.Field(NrdbResultContainer, graphql_name='nrdbQuery', args=sgqlc.types.ArgDict((
        ('nrql', sgqlc.types.Arg(sgqlc.types.non_null(Nrql), graphql_name='nrql', default=None)),
        ('timeout', sgqlc.types.Arg(Seconds, graphql_name='timeout', default=None)),
))
    )
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    port_or_path = sgqlc.types.Field(String, graphql_name='portOrPath')
    relationships = sgqlc.types.Field(sgqlc.types.list_of(EntityRelationship), graphql_name='relationships', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(EpochMilliseconds, graphql_name='endTime', default=None)),
        ('filter', sgqlc.types.Arg(EntityRelationshipFilter, graphql_name='filter', default=None)),
))
    )
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')
    vendor = sgqlc.types.Field(String, graphql_name='vendor')


class ApmDatabaseInstanceEntityOutline(sgqlc.types.Type, EntityOutline):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    host = sgqlc.types.Field(String, graphql_name='host')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    port_or_path = sgqlc.types.Field(String, graphql_name='portOrPath')
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')
    vendor = sgqlc.types.Field(String, graphql_name='vendor')


class ApmExternalServiceEntity(sgqlc.types.Type, Entity):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    external_summary = sgqlc.types.Field(ApmExternalServiceSummaryData, graphql_name='externalSummary')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    host = sgqlc.types.Field(String, graphql_name='host')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    nerd_storage = sgqlc.types.Field(NerdStorageEntityScope, graphql_name='nerdStorage')
    nrdb_query = sgqlc.types.Field(NrdbResultContainer, graphql_name='nrdbQuery', args=sgqlc.types.ArgDict((
        ('nrql', sgqlc.types.Arg(sgqlc.types.non_null(Nrql), graphql_name='nrql', default=None)),
        ('timeout', sgqlc.types.Arg(Seconds, graphql_name='timeout', default=None)),
))
    )
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    relationships = sgqlc.types.Field(sgqlc.types.list_of(EntityRelationship), graphql_name='relationships', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(EpochMilliseconds, graphql_name='endTime', default=None)),
        ('filter', sgqlc.types.Arg(EntityRelationshipFilter, graphql_name='filter', default=None)),
))
    )
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class ApmExternalServiceEntityOutline(sgqlc.types.Type, EntityOutline):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    external_summary = sgqlc.types.Field(ApmExternalServiceSummaryData, graphql_name='externalSummary')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    host = sgqlc.types.Field(String, graphql_name='host')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class BrowserApplicationEntity(sgqlc.types.Type, AlertableEntity, Entity):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    alert_severity = sgqlc.types.Field(EntityAlertSeverity, graphql_name='alertSeverity')
    alert_violations = sgqlc.types.Field(sgqlc.types.list_of(EntityAlertViolation), graphql_name='alertViolations', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(sgqlc.types.non_null(EpochMilliseconds), graphql_name='endTime', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(EpochMilliseconds), graphql_name='startTime', default=None)),
))
    )
    application_id = sgqlc.types.Field(Int, graphql_name='applicationId')
    browser_summary = sgqlc.types.Field(BrowserApplicationSummaryData, graphql_name='browserSummary')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    nerd_storage = sgqlc.types.Field(NerdStorageEntityScope, graphql_name='nerdStorage')
    nrdb_query = sgqlc.types.Field(NrdbResultContainer, graphql_name='nrdbQuery', args=sgqlc.types.ArgDict((
        ('nrql', sgqlc.types.Arg(sgqlc.types.non_null(Nrql), graphql_name='nrql', default=None)),
        ('timeout', sgqlc.types.Arg(Seconds, graphql_name='timeout', default=None)),
))
    )
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    recent_alert_violations = sgqlc.types.Field(sgqlc.types.list_of(EntityAlertViolation), graphql_name='recentAlertViolations', args=sgqlc.types.ArgDict((
        ('count', sgqlc.types.Arg(Int, graphql_name='count', default=10)),
))
    )
    relationships = sgqlc.types.Field(sgqlc.types.list_of(EntityRelationship), graphql_name='relationships', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(EpochMilliseconds, graphql_name='endTime', default=None)),
        ('filter', sgqlc.types.Arg(EntityRelationshipFilter, graphql_name='filter', default=None)),
))
    )
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    running_agent_versions = sgqlc.types.Field(BrowserApplicationRunningAgentVersions, graphql_name='runningAgentVersions')
    serving_apm_application_id = sgqlc.types.Field(Int, graphql_name='servingApmApplicationId')
    settings = sgqlc.types.Field(BrowserApplicationSettings, graphql_name='settings')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class BrowserApplicationEntityOutline(sgqlc.types.Type, AlertableEntityOutline, EntityOutline):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    alert_severity = sgqlc.types.Field(EntityAlertSeverity, graphql_name='alertSeverity')
    application_id = sgqlc.types.Field(Int, graphql_name='applicationId')
    browser_summary = sgqlc.types.Field(BrowserApplicationSummaryData, graphql_name='browserSummary')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    running_agent_versions = sgqlc.types.Field(BrowserApplicationRunningAgentVersions, graphql_name='runningAgentVersions')
    serving_apm_application_id = sgqlc.types.Field(Int, graphql_name='servingApmApplicationId')
    settings = sgqlc.types.Field(BrowserApplicationSettings, graphql_name='settings')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class CloudAlbIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    load_balancer_prefixes = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='loadBalancerPrefixes')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudApigatewayIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    stage_prefixes = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stagePrefixes')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudAutoscalingIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudAwsProvider(sgqlc.types.Type, CloudProvider):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    icon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='icon')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    role_account_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='roleAccountId')
    role_external_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='roleExternalId')
    service = sgqlc.types.Field(CloudService, graphql_name='service', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
))
    )
    services = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CloudService))), graphql_name='services')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudAzureAppserviceIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudAzureCosmosdbIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudAzureFunctionsIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudAzureLoadbalancerIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudAzureMariadbIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudAzureMysqlIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudAzurePostgresqlIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudAzureRediscacheIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudAzureServicebusIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudAzureSqlIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudAzureStorageIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudAzureVirtualnetworksIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudAzureVmsIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    resource_groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='resourceGroups')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudBaseIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudBaseProvider(sgqlc.types.Type, CloudProvider):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    icon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='icon')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    service = sgqlc.types.Field(CloudService, graphql_name='service', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
))
    )
    services = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CloudService))), graphql_name='services')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudBillingIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudCloudfrontIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_lambdas_at_edge = sgqlc.types.Field(Boolean, graphql_name='fetchLambdasAtEdge')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudCloudtrailIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudDynamodbIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudEbsIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudEc2Integration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_ip_addresses = sgqlc.types.Field(Boolean, graphql_name='fetchIpAddresses')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudEcsIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudEfsIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudElasticacheIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudElasticbeanstalkIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudElasticsearchIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_nodes = sgqlc.types.Field(Boolean, graphql_name='fetchNodes')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudElbIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudEmrIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudGcpAppengineIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudGcpBigqueryIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudGcpFunctionsIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudGcpKubernetesIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudGcpLoadbalancingIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudGcpProvider(sgqlc.types.Type, CloudProvider):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    icon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='icon')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    service = sgqlc.types.Field(CloudService, graphql_name='service', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
))
    )
    service_account_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='serviceAccountId')
    services = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CloudService))), graphql_name='services')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudGcpPubsubIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudGcpSpannerIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudGcpSqlIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudGcpStorageIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudGcpVmsIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudHealthIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudIamIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudIotIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudKinesisFirehoseIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudKinesisIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_shards = sgqlc.types.Field(Boolean, graphql_name='fetchShards')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudLambdaIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudRdsIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudRedshiftIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudRoute53Integration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudS3Integration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudSesIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudSnsIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudSqsIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_extended_inventory = sgqlc.types.Field(Boolean, graphql_name='fetchExtendedInventory')
    fetch_tags = sgqlc.types.Field(Boolean, graphql_name='fetchTags')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    queue_prefixes = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='queuePrefixes')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class CloudVpcIntegration(sgqlc.types.Type, CloudIntegration):
    __schema__ = newrelic_schema
    aws_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='awsRegions')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='createdAt')
    fetch_nat_gateway = sgqlc.types.Field(Boolean, graphql_name='fetchNatGateway')
    fetch_vpn = sgqlc.types.Field(Boolean, graphql_name='fetchVpn')
    id = sgqlc.types.Field(Int, graphql_name='id')
    inventory_polling_interval = sgqlc.types.Field(Int, graphql_name='inventoryPollingInterval')
    linked_account = sgqlc.types.Field(CloudLinkedAccount, graphql_name='linkedAccount')
    metrics_polling_interval = sgqlc.types.Field(Int, graphql_name='metricsPollingInterval')
    name = sgqlc.types.Field(String, graphql_name='name')
    nr_account_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nrAccountId')
    service = sgqlc.types.Field(CloudService, graphql_name='service')
    tag_key = sgqlc.types.Field(String, graphql_name='tagKey')
    tag_value = sgqlc.types.Field(String, graphql_name='tagValue')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(EpochSeconds), graphql_name='updatedAt')


class DashboardEntity(sgqlc.types.Type, Entity):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    nerd_storage = sgqlc.types.Field(NerdStorageEntityScope, graphql_name='nerdStorage')
    nrdb_query = sgqlc.types.Field(NrdbResultContainer, graphql_name='nrdbQuery', args=sgqlc.types.ArgDict((
        ('nrql', sgqlc.types.Arg(sgqlc.types.non_null(Nrql), graphql_name='nrql', default=None)),
        ('timeout', sgqlc.types.Arg(Seconds, graphql_name='timeout', default=None)),
))
    )
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    relationships = sgqlc.types.Field(sgqlc.types.list_of(EntityRelationship), graphql_name='relationships', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(EpochMilliseconds, graphql_name='endTime', default=None)),
        ('filter', sgqlc.types.Arg(EntityRelationshipFilter, graphql_name='filter', default=None)),
))
    )
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class DashboardEntityOutline(sgqlc.types.Type, EntityOutline):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class GenericEntity(sgqlc.types.Type, Entity):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    nerd_storage = sgqlc.types.Field(NerdStorageEntityScope, graphql_name='nerdStorage')
    nrdb_query = sgqlc.types.Field(NrdbResultContainer, graphql_name='nrdbQuery', args=sgqlc.types.ArgDict((
        ('nrql', sgqlc.types.Arg(sgqlc.types.non_null(Nrql), graphql_name='nrql', default=None)),
        ('timeout', sgqlc.types.Arg(Seconds, graphql_name='timeout', default=None)),
))
    )
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    relationships = sgqlc.types.Field(sgqlc.types.list_of(EntityRelationship), graphql_name='relationships', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(EpochMilliseconds, graphql_name='endTime', default=None)),
        ('filter', sgqlc.types.Arg(EntityRelationshipFilter, graphql_name='filter', default=None)),
))
    )
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class GenericEntityOutline(sgqlc.types.Type, EntityOutline):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class GenericInfrastructureEntity(sgqlc.types.Type, InfrastructureIntegrationEntity, AlertableEntity, Entity):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    alert_severity = sgqlc.types.Field(EntityAlertSeverity, graphql_name='alertSeverity')
    alert_violations = sgqlc.types.Field(sgqlc.types.list_of(EntityAlertViolation), graphql_name='alertViolations', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(sgqlc.types.non_null(EpochMilliseconds), graphql_name='endTime', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(EpochMilliseconds), graphql_name='startTime', default=None)),
))
    )
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    integration_type_code = sgqlc.types.Field(String, graphql_name='integrationTypeCode')
    name = sgqlc.types.Field(String, graphql_name='name')
    nerd_storage = sgqlc.types.Field(NerdStorageEntityScope, graphql_name='nerdStorage')
    nrdb_query = sgqlc.types.Field(NrdbResultContainer, graphql_name='nrdbQuery', args=sgqlc.types.ArgDict((
        ('nrql', sgqlc.types.Arg(sgqlc.types.non_null(Nrql), graphql_name='nrql', default=None)),
        ('timeout', sgqlc.types.Arg(Seconds, graphql_name='timeout', default=None)),
))
    )
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    recent_alert_violations = sgqlc.types.Field(sgqlc.types.list_of(EntityAlertViolation), graphql_name='recentAlertViolations', args=sgqlc.types.ArgDict((
        ('count', sgqlc.types.Arg(Int, graphql_name='count', default=10)),
))
    )
    relationships = sgqlc.types.Field(sgqlc.types.list_of(EntityRelationship), graphql_name='relationships', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(EpochMilliseconds, graphql_name='endTime', default=None)),
        ('filter', sgqlc.types.Arg(EntityRelationshipFilter, graphql_name='filter', default=None)),
))
    )
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class GenericInfrastructureEntityOutline(sgqlc.types.Type, InfrastructureIntegrationEntityOutline, AlertableEntityOutline, EntityOutline):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    alert_severity = sgqlc.types.Field(EntityAlertSeverity, graphql_name='alertSeverity')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    integration_type_code = sgqlc.types.Field(String, graphql_name='integrationTypeCode')
    name = sgqlc.types.Field(String, graphql_name='name')
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class InfrastructureAwsLambdaFunctionEntity(sgqlc.types.Type, InfrastructureIntegrationEntity, AlertableEntity, Entity):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    alert_severity = sgqlc.types.Field(EntityAlertSeverity, graphql_name='alertSeverity')
    alert_violations = sgqlc.types.Field(sgqlc.types.list_of(EntityAlertViolation), graphql_name='alertViolations', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(sgqlc.types.non_null(EpochMilliseconds), graphql_name='endTime', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(EpochMilliseconds), graphql_name='startTime', default=None)),
))
    )
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    integration_type_code = sgqlc.types.Field(String, graphql_name='integrationTypeCode')
    name = sgqlc.types.Field(String, graphql_name='name')
    nerd_storage = sgqlc.types.Field(NerdStorageEntityScope, graphql_name='nerdStorage')
    nrdb_query = sgqlc.types.Field(NrdbResultContainer, graphql_name='nrdbQuery', args=sgqlc.types.ArgDict((
        ('nrql', sgqlc.types.Arg(sgqlc.types.non_null(Nrql), graphql_name='nrql', default=None)),
        ('timeout', sgqlc.types.Arg(Seconds, graphql_name='timeout', default=None)),
))
    )
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    recent_alert_violations = sgqlc.types.Field(sgqlc.types.list_of(EntityAlertViolation), graphql_name='recentAlertViolations', args=sgqlc.types.ArgDict((
        ('count', sgqlc.types.Arg(Int, graphql_name='count', default=10)),
))
    )
    relationships = sgqlc.types.Field(sgqlc.types.list_of(EntityRelationship), graphql_name='relationships', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(EpochMilliseconds, graphql_name='endTime', default=None)),
        ('filter', sgqlc.types.Arg(EntityRelationshipFilter, graphql_name='filter', default=None)),
))
    )
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    runtime = sgqlc.types.Field(String, graphql_name='runtime')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class InfrastructureAwsLambdaFunctionEntityOutline(sgqlc.types.Type, InfrastructureIntegrationEntityOutline, AlertableEntityOutline, EntityOutline):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    alert_severity = sgqlc.types.Field(EntityAlertSeverity, graphql_name='alertSeverity')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    integration_type_code = sgqlc.types.Field(String, graphql_name='integrationTypeCode')
    name = sgqlc.types.Field(String, graphql_name='name')
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    runtime = sgqlc.types.Field(String, graphql_name='runtime')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class InfrastructureHostEntity(sgqlc.types.Type, AlertableEntity, Entity):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    alert_severity = sgqlc.types.Field(EntityAlertSeverity, graphql_name='alertSeverity')
    alert_violations = sgqlc.types.Field(sgqlc.types.list_of(EntityAlertViolation), graphql_name='alertViolations', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(sgqlc.types.non_null(EpochMilliseconds), graphql_name='endTime', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(EpochMilliseconds), graphql_name='startTime', default=None)),
))
    )
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    host_summary = sgqlc.types.Field(InfrastructureHostSummaryData, graphql_name='hostSummary')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    nerd_storage = sgqlc.types.Field(NerdStorageEntityScope, graphql_name='nerdStorage')
    nrdb_query = sgqlc.types.Field(NrdbResultContainer, graphql_name='nrdbQuery', args=sgqlc.types.ArgDict((
        ('nrql', sgqlc.types.Arg(sgqlc.types.non_null(Nrql), graphql_name='nrql', default=None)),
        ('timeout', sgqlc.types.Arg(Seconds, graphql_name='timeout', default=None)),
))
    )
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    recent_alert_violations = sgqlc.types.Field(sgqlc.types.list_of(EntityAlertViolation), graphql_name='recentAlertViolations', args=sgqlc.types.ArgDict((
        ('count', sgqlc.types.Arg(Int, graphql_name='count', default=10)),
))
    )
    relationships = sgqlc.types.Field(sgqlc.types.list_of(EntityRelationship), graphql_name='relationships', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(EpochMilliseconds, graphql_name='endTime', default=None)),
        ('filter', sgqlc.types.Arg(EntityRelationshipFilter, graphql_name='filter', default=None)),
))
    )
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class InfrastructureHostEntityOutline(sgqlc.types.Type, AlertableEntityOutline, EntityOutline):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    alert_severity = sgqlc.types.Field(EntityAlertSeverity, graphql_name='alertSeverity')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    host_summary = sgqlc.types.Field(InfrastructureHostSummaryData, graphql_name='hostSummary')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class MobileApplicationEntity(sgqlc.types.Type, AlertableEntity, Entity):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    alert_severity = sgqlc.types.Field(EntityAlertSeverity, graphql_name='alertSeverity')
    alert_violations = sgqlc.types.Field(sgqlc.types.list_of(EntityAlertViolation), graphql_name='alertViolations', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(sgqlc.types.non_null(EpochMilliseconds), graphql_name='endTime', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(EpochMilliseconds), graphql_name='startTime', default=None)),
))
    )
    application_id = sgqlc.types.Field(Int, graphql_name='applicationId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    mobile_summary = sgqlc.types.Field(MobileAppSummaryData, graphql_name='mobileSummary')
    name = sgqlc.types.Field(String, graphql_name='name')
    nerd_storage = sgqlc.types.Field(NerdStorageEntityScope, graphql_name='nerdStorage')
    nrdb_query = sgqlc.types.Field(NrdbResultContainer, graphql_name='nrdbQuery', args=sgqlc.types.ArgDict((
        ('nrql', sgqlc.types.Arg(sgqlc.types.non_null(Nrql), graphql_name='nrql', default=None)),
        ('timeout', sgqlc.types.Arg(Seconds, graphql_name='timeout', default=None)),
))
    )
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    recent_alert_violations = sgqlc.types.Field(sgqlc.types.list_of(EntityAlertViolation), graphql_name='recentAlertViolations', args=sgqlc.types.ArgDict((
        ('count', sgqlc.types.Arg(Int, graphql_name='count', default=10)),
))
    )
    relationships = sgqlc.types.Field(sgqlc.types.list_of(EntityRelationship), graphql_name='relationships', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(EpochMilliseconds, graphql_name='endTime', default=None)),
        ('filter', sgqlc.types.Arg(EntityRelationshipFilter, graphql_name='filter', default=None)),
))
    )
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class MobileApplicationEntityOutline(sgqlc.types.Type, AlertableEntityOutline, EntityOutline):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    alert_severity = sgqlc.types.Field(EntityAlertSeverity, graphql_name='alertSeverity')
    application_id = sgqlc.types.Field(Int, graphql_name='applicationId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    mobile_summary = sgqlc.types.Field(MobileAppSummaryData, graphql_name='mobileSummary')
    name = sgqlc.types.Field(String, graphql_name='name')
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class SuggestedAnomalyBasedNrqlQuery(sgqlc.types.Type, SuggestedNrqlQuery):
    __schema__ = newrelic_schema
    anomaly = sgqlc.types.Field(sgqlc.types.non_null(SuggestedNrqlQueryAnomaly), graphql_name='anomaly')
    nrql = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nrql')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class SuggestedHistoryBasedNrqlQuery(sgqlc.types.Type, SuggestedNrqlQuery):
    __schema__ = newrelic_schema
    nrql = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nrql')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class SyntheticMonitorEntity(sgqlc.types.Type, Entity):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    frequency = sgqlc.types.Field(Minutes, graphql_name='frequency')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    monitor_id = sgqlc.types.Field(ID, graphql_name='monitorId')
    monitor_summary = sgqlc.types.Field(SyntheticMonitorSummaryData, graphql_name='monitorSummary')
    monitor_type = sgqlc.types.Field(SyntheticMonitorType, graphql_name='monitorType')
    name = sgqlc.types.Field(String, graphql_name='name')
    nerd_storage = sgqlc.types.Field(NerdStorageEntityScope, graphql_name='nerdStorage')
    nrdb_query = sgqlc.types.Field(NrdbResultContainer, graphql_name='nrdbQuery', args=sgqlc.types.ArgDict((
        ('nrql', sgqlc.types.Arg(sgqlc.types.non_null(Nrql), graphql_name='nrql', default=None)),
        ('timeout', sgqlc.types.Arg(Seconds, graphql_name='timeout', default=None)),
))
    )
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    relationships = sgqlc.types.Field(sgqlc.types.list_of(EntityRelationship), graphql_name='relationships', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(EpochMilliseconds, graphql_name='endTime', default=None)),
        ('filter', sgqlc.types.Arg(EntityRelationshipFilter, graphql_name='filter', default=None)),
))
    )
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class SyntheticMonitorEntityOutline(sgqlc.types.Type, EntityOutline):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    frequency = sgqlc.types.Field(Minutes, graphql_name='frequency')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    monitor_id = sgqlc.types.Field(ID, graphql_name='monitorId')
    monitor_summary = sgqlc.types.Field(SyntheticMonitorSummaryData, graphql_name='monitorSummary')
    monitor_type = sgqlc.types.Field(SyntheticMonitorType, graphql_name='monitorType')
    name = sgqlc.types.Field(String, graphql_name='name')
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class UnavailableEntity(sgqlc.types.Type, Entity):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    nerd_storage = sgqlc.types.Field(NerdStorageEntityScope, graphql_name='nerdStorage')
    nrdb_query = sgqlc.types.Field(NrdbResultContainer, graphql_name='nrdbQuery', args=sgqlc.types.ArgDict((
        ('nrql', sgqlc.types.Arg(sgqlc.types.non_null(Nrql), graphql_name='nrql', default=None)),
        ('timeout', sgqlc.types.Arg(Seconds, graphql_name='timeout', default=None)),
))
    )
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    relationships = sgqlc.types.Field(sgqlc.types.list_of(EntityRelationship), graphql_name='relationships', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(EpochMilliseconds, graphql_name='endTime', default=None)),
        ('filter', sgqlc.types.Arg(EntityRelationshipFilter, graphql_name='filter', default=None)),
))
    )
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class UnavailableEntityOutline(sgqlc.types.Type, EntityOutline):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class WorkloadEntity(sgqlc.types.Type, Entity):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    nerd_storage = sgqlc.types.Field(NerdStorageEntityScope, graphql_name='nerdStorage')
    nrdb_query = sgqlc.types.Field(NrdbResultContainer, graphql_name='nrdbQuery', args=sgqlc.types.ArgDict((
        ('nrql', sgqlc.types.Arg(sgqlc.types.non_null(Nrql), graphql_name='nrql', default=None)),
        ('timeout', sgqlc.types.Arg(Seconds, graphql_name='timeout', default=None)),
))
    )
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    relationships = sgqlc.types.Field(sgqlc.types.list_of(EntityRelationship), graphql_name='relationships', args=sgqlc.types.ArgDict((
        ('end_time', sgqlc.types.Arg(EpochMilliseconds, graphql_name='endTime', default=None)),
        ('filter', sgqlc.types.Arg(EntityRelationshipFilter, graphql_name='filter', default=None)),
))
    )
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')


class WorkloadEntityOutline(sgqlc.types.Type, EntityOutline):
    __schema__ = newrelic_schema
    account = sgqlc.types.Field(AccountOutline, graphql_name='account')
    account_id = sgqlc.types.Field(Int, graphql_name='accountId')
    domain = sgqlc.types.Field(String, graphql_name='domain')
    entity_type = sgqlc.types.Field(EntityType, graphql_name='entityType')
    guid = sgqlc.types.Field(EntityGuid, graphql_name='guid')
    indexed_at = sgqlc.types.Field(EpochMilliseconds, graphql_name='indexedAt')
    name = sgqlc.types.Field(String, graphql_name='name')
    permalink = sgqlc.types.Field(String, graphql_name='permalink')
    reporting = sgqlc.types.Field(Boolean, graphql_name='reporting')
    tags = sgqlc.types.Field(sgqlc.types.list_of(EntityTag), graphql_name='tags')
    type = sgqlc.types.Field(String, graphql_name='type')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
newrelic_schema.query_type = RootQueryType
newrelic_schema.mutation_type = RootMutationType
newrelic_schema.subscription_type = None

