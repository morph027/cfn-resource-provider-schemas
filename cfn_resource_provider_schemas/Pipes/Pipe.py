SCHEMA = {
  "typeName" : "AWS::Pipes::Pipe",
  "description" : "Definition of AWS::Pipes::Pipe Resource Type",
  "definitions" : {
    "AssignPublicIp" : {
      "type" : "string",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "AwsVpcConfiguration" : {
      "type" : "object",
      "properties" : {
        "Subnets" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 1024,
            "minLength" : 1,
            "pattern" : "^subnet-[0-9a-z]*|(\\$(\\.[\\w/_-]+(\\[(\\d+|\\*)\\])*)*)$"
          },
          "maxItems" : 16,
          "minItems" : 0
        },
        "SecurityGroups" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 1024,
            "minLength" : 1,
            "pattern" : "^sg-[0-9a-zA-Z]*|(\\$(\\.[\\w/_-]+(\\[(\\d+|\\*)\\])*)*)$"
          },
          "maxItems" : 5,
          "minItems" : 0
        },
        "AssignPublicIp" : {
          "$ref" : "#/definitions/AssignPublicIp"
        }
      },
      "required" : [ "Subnets" ],
      "additionalProperties" : False
    },
    "BatchArrayProperties" : {
      "type" : "object",
      "properties" : {
        "Size" : {
          "type" : "integer",
          "default" : 0,
          "maximum" : 10000,
          "minimum" : 2
        }
      },
      "additionalProperties" : False
    },
    "BatchContainerOverrides" : {
      "type" : "object",
      "properties" : {
        "Command" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "Environment" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/BatchEnvironmentVariable"
          }
        },
        "InstanceType" : {
          "type" : "string"
        },
        "ResourceRequirements" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/BatchResourceRequirement"
          }
        }
      },
      "additionalProperties" : False
    },
    "BatchEnvironmentVariable" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "BatchJobDependency" : {
      "type" : "object",
      "properties" : {
        "JobId" : {
          "type" : "string"
        },
        "Type" : {
          "$ref" : "#/definitions/BatchJobDependencyType"
        }
      },
      "additionalProperties" : False
    },
    "BatchJobDependencyType" : {
      "type" : "string",
      "enum" : [ "N_TO_N", "SEQUENTIAL" ]
    },
    "BatchParametersMap" : {
      "type" : "object",
      "patternProperties" : {
        ".+" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "BatchResourceRequirement" : {
      "type" : "object",
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/BatchResourceRequirementType"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "required" : [ "Type", "Value" ],
      "additionalProperties" : False
    },
    "BatchResourceRequirementType" : {
      "type" : "string",
      "enum" : [ "GPU", "MEMORY", "VCPU" ]
    },
    "BatchRetryStrategy" : {
      "type" : "object",
      "properties" : {
        "Attempts" : {
          "type" : "integer",
          "default" : 0,
          "maximum" : 10,
          "minimum" : 1
        }
      },
      "additionalProperties" : False
    },
    "CapacityProviderStrategyItem" : {
      "type" : "object",
      "properties" : {
        "CapacityProvider" : {
          "type" : "string",
          "maxLength" : 255,
          "minLength" : 1
        },
        "Weight" : {
          "type" : "integer",
          "default" : 0,
          "maximum" : 1000,
          "minimum" : 0
        },
        "Base" : {
          "type" : "integer",
          "default" : 0,
          "maximum" : 100000,
          "minimum" : 0
        }
      },
      "required" : [ "CapacityProvider" ],
      "additionalProperties" : False
    },
    "CloudwatchLogsLogDestination" : {
      "type" : "object",
      "properties" : {
        "LogGroupArn" : {
          "type" : "string",
          "maxLength" : 1600,
          "minLength" : 1,
          "pattern" : "^(^arn:aws([a-z]|\\-)*:logs:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1}):(\\d{12}):log-group:.+)$"
        }
      },
      "additionalProperties" : False
    },
    "DeadLetterConfig" : {
      "type" : "object",
      "properties" : {
        "Arn" : {
          "type" : "string",
          "maxLength" : 1600,
          "minLength" : 1,
          "pattern" : "^arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\\-]+):([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1})?:(\\d{12})?:(.+)$"
        }
      },
      "additionalProperties" : False
    },
    "DimensionMapping" : {
      "type" : "object",
      "properties" : {
        "DimensionValue" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 1
        },
        "DimensionValueType" : {
          "$ref" : "#/definitions/DimensionValueType"
        },
        "DimensionName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1
        }
      },
      "required" : [ "DimensionName", "DimensionValue", "DimensionValueType" ],
      "additionalProperties" : False
    },
    "DimensionValueType" : {
      "type" : "string",
      "enum" : [ "VARCHAR" ]
    },
    "DynamoDBStreamStartPosition" : {
      "type" : "string",
      "enum" : [ "TRIM_HORIZON", "LATEST" ]
    },
    "EcsContainerOverride" : {
      "type" : "object",
      "properties" : {
        "Command" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          }
        },
        "Cpu" : {
          "type" : "integer"
        },
        "Environment" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/EcsEnvironmentVariable"
          }
        },
        "EnvironmentFiles" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/EcsEnvironmentFile"
          }
        },
        "Memory" : {
          "type" : "integer"
        },
        "MemoryReservation" : {
          "type" : "integer"
        },
        "Name" : {
          "type" : "string"
        },
        "ResourceRequirements" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/EcsResourceRequirement"
          }
        }
      },
      "additionalProperties" : False
    },
    "EcsEnvironmentFile" : {
      "type" : "object",
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/EcsEnvironmentFileType"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "required" : [ "Type", "Value" ],
      "additionalProperties" : False
    },
    "EcsEnvironmentFileType" : {
      "type" : "string",
      "enum" : [ "s3" ]
    },
    "EcsEnvironmentVariable" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "EcsEphemeralStorage" : {
      "type" : "object",
      "properties" : {
        "SizeInGiB" : {
          "type" : "integer",
          "default" : 0,
          "maximum" : 200,
          "minimum" : 21
        }
      },
      "required" : [ "SizeInGiB" ],
      "additionalProperties" : False
    },
    "EcsInferenceAcceleratorOverride" : {
      "type" : "object",
      "properties" : {
        "DeviceName" : {
          "type" : "string"
        },
        "DeviceType" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "EcsResourceRequirement" : {
      "type" : "object",
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/EcsResourceRequirementType"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "required" : [ "Type", "Value" ],
      "additionalProperties" : False
    },
    "EcsResourceRequirementType" : {
      "type" : "string",
      "enum" : [ "GPU", "InferenceAccelerator" ]
    },
    "EcsTaskOverride" : {
      "type" : "object",
      "properties" : {
        "ContainerOverrides" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/EcsContainerOverride"
          }
        },
        "Cpu" : {
          "type" : "string"
        },
        "EphemeralStorage" : {
          "$ref" : "#/definitions/EcsEphemeralStorage"
        },
        "ExecutionRoleArn" : {
          "type" : "string",
          "maxLength" : 1600,
          "minLength" : 1,
          "pattern" : "^arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\\-]+):([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1})?:(\\d{12})?:(.+)|(\\$(\\.[\\w/_-]+(\\[(\\d+|\\*)\\])*)*)$"
        },
        "InferenceAcceleratorOverrides" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/EcsInferenceAcceleratorOverride"
          }
        },
        "Memory" : {
          "type" : "string"
        },
        "TaskRoleArn" : {
          "type" : "string",
          "maxLength" : 1600,
          "minLength" : 1,
          "pattern" : "^arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\\-]+):([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1})?:(\\d{12})?:(.+)|(\\$(\\.[\\w/_-]+(\\[(\\d+|\\*)\\])*)*)$"
        }
      },
      "additionalProperties" : False
    },
    "EpochTimeUnit" : {
      "type" : "string",
      "enum" : [ "MILLISECONDS", "SECONDS", "MICROSECONDS", "NANOSECONDS" ]
    },
    "Filter" : {
      "type" : "object",
      "properties" : {
        "Pattern" : {
          "type" : "string",
          "maxLength" : 4096,
          "minLength" : 0
        }
      },
      "additionalProperties" : False
    },
    "FilterCriteria" : {
      "type" : "object",
      "properties" : {
        "Filters" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/Filter"
          },
          "maxItems" : 5,
          "minItems" : 0
        }
      },
      "additionalProperties" : False
    },
    "FirehoseLogDestination" : {
      "type" : "object",
      "properties" : {
        "DeliveryStreamArn" : {
          "type" : "string",
          "maxLength" : 1600,
          "minLength" : 1,
          "pattern" : "^(^arn:aws([a-z]|\\-)*:firehose:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1}):(\\d{12}):deliverystream/.+)$"
        }
      },
      "additionalProperties" : False
    },
    "HeaderParametersMap" : {
      "type" : "object",
      "patternProperties" : {
        "^[!#$%&'*+-.^_`|~0-9a-zA-Z]+|(\\$(\\.[\\w/_-]+(\\[(\\d+|\\*)\\])*)*)$" : {
          "type" : "string",
          "maxLength" : 512,
          "minLength" : 0,
          "pattern" : "^[ \\t]*[\\x20-\\x7E]+([ \\t]+[\\x20-\\x7E]+)*[ \\t]*|(\\$(\\.[\\w/_-]+(\\[(\\d+|\\*)\\])*)*)$"
        }
      },
      "additionalProperties" : False
    },
    "IncludeExecutionDataOption" : {
      "type" : "string",
      "enum" : [ "ALL" ]
    },
    "KinesisStreamStartPosition" : {
      "type" : "string",
      "enum" : [ "TRIM_HORIZON", "LATEST", "AT_TIMESTAMP" ]
    },
    "LaunchType" : {
      "type" : "string",
      "enum" : [ "EC2", "FARGATE", "EXTERNAL" ]
    },
    "LogLevel" : {
      "type" : "string",
      "enum" : [ "OFF", "ERROR", "INFO", "TRACE" ]
    },
    "MQBrokerAccessCredentials" : {
      "oneOf" : [ {
        "type" : "object",
        "title" : "BasicAuth",
        "properties" : {
          "BasicAuth" : {
            "type" : "string",
            "maxLength" : 1600,
            "minLength" : 1,
            "pattern" : "^(^arn:aws([a-z]|\\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1}):(\\d{12}):secret:.+)$",
            "description" : "Optional SecretManager ARN which stores the database credentials"
          }
        },
        "required" : [ "BasicAuth" ],
        "additionalProperties" : False
      } ]
    },
    "MSKAccessCredentials" : {
      "oneOf" : [ {
        "type" : "object",
        "title" : "SaslScram512Auth",
        "properties" : {
          "SaslScram512Auth" : {
            "type" : "string",
            "maxLength" : 1600,
            "minLength" : 1,
            "pattern" : "^(^arn:aws([a-z]|\\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1}):(\\d{12}):secret:.+)$",
            "description" : "Optional SecretManager ARN which stores the database credentials"
          }
        },
        "required" : [ "SaslScram512Auth" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "ClientCertificateTlsAuth",
        "properties" : {
          "ClientCertificateTlsAuth" : {
            "type" : "string",
            "maxLength" : 1600,
            "minLength" : 1,
            "pattern" : "^(^arn:aws([a-z]|\\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1}):(\\d{12}):secret:.+)$",
            "description" : "Optional SecretManager ARN which stores the database credentials"
          }
        },
        "required" : [ "ClientCertificateTlsAuth" ],
        "additionalProperties" : False
      } ]
    },
    "MSKStartPosition" : {
      "type" : "string",
      "enum" : [ "TRIM_HORIZON", "LATEST" ]
    },
    "MeasureValueType" : {
      "type" : "string",
      "enum" : [ "DOUBLE", "BIGINT", "VARCHAR", "BOOLEAN", "TIMESTAMP" ]
    },
    "MultiMeasureAttributeMapping" : {
      "type" : "object",
      "properties" : {
        "MeasureValue" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 1
        },
        "MeasureValueType" : {
          "$ref" : "#/definitions/MeasureValueType"
        },
        "MultiMeasureAttributeName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1
        }
      },
      "required" : [ "MeasureValue", "MeasureValueType", "MultiMeasureAttributeName" ],
      "additionalProperties" : False
    },
    "MultiMeasureMapping" : {
      "type" : "object",
      "properties" : {
        "MultiMeasureName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1
        },
        "MultiMeasureAttributeMappings" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/MultiMeasureAttributeMapping"
          },
          "maxItems" : 256,
          "minItems" : 1
        }
      },
      "required" : [ "MultiMeasureAttributeMappings", "MultiMeasureName" ],
      "additionalProperties" : False
    },
    "NetworkConfiguration" : {
      "type" : "object",
      "properties" : {
        "AwsvpcConfiguration" : {
          "$ref" : "#/definitions/AwsVpcConfiguration"
        }
      },
      "additionalProperties" : False
    },
    "OnPartialBatchItemFailureStreams" : {
      "type" : "string",
      "enum" : [ "AUTOMATIC_BISECT" ]
    },
    "PipeEnrichmentHttpParameters" : {
      "type" : "object",
      "properties" : {
        "PathParameterValues" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "pattern" : "^(?!\\s*$).+|(\\$(\\.[\\w/_-]+(\\[(\\d+|\\*)\\])*)*)$"
          }
        },
        "HeaderParameters" : {
          "$ref" : "#/definitions/HeaderParametersMap"
        },
        "QueryStringParameters" : {
          "$ref" : "#/definitions/QueryStringParametersMap"
        }
      },
      "additionalProperties" : False
    },
    "PipeEnrichmentParameters" : {
      "type" : "object",
      "properties" : {
        "InputTemplate" : {
          "type" : "string",
          "maxLength" : 8192,
          "minLength" : 0
        },
        "HttpParameters" : {
          "$ref" : "#/definitions/PipeEnrichmentHttpParameters"
        }
      },
      "additionalProperties" : False
    },
    "PipeLogConfiguration" : {
      "type" : "object",
      "properties" : {
        "S3LogDestination" : {
          "$ref" : "#/definitions/S3LogDestination"
        },
        "FirehoseLogDestination" : {
          "$ref" : "#/definitions/FirehoseLogDestination"
        },
        "CloudwatchLogsLogDestination" : {
          "$ref" : "#/definitions/CloudwatchLogsLogDestination"
        },
        "Level" : {
          "$ref" : "#/definitions/LogLevel"
        },
        "IncludeExecutionData" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/IncludeExecutionDataOption"
          },
          "uniqueItems" : True
        }
      },
      "additionalProperties" : False
    },
    "PipeSourceActiveMQBrokerParameters" : {
      "type" : "object",
      "properties" : {
        "Credentials" : {
          "$ref" : "#/definitions/MQBrokerAccessCredentials"
        },
        "QueueName" : {
          "type" : "string",
          "maxLength" : 1000,
          "minLength" : 1,
          "pattern" : "^[\\s\\S]*$"
        },
        "BatchSize" : {
          "type" : "integer",
          "maximum" : 10000,
          "minimum" : 1
        },
        "MaximumBatchingWindowInSeconds" : {
          "type" : "integer",
          "maximum" : 300,
          "minimum" : 0
        }
      },
      "required" : [ "Credentials", "QueueName" ],
      "additionalProperties" : False
    },
    "PipeSourceDynamoDBStreamParameters" : {
      "type" : "object",
      "properties" : {
        "BatchSize" : {
          "type" : "integer",
          "maximum" : 10000,
          "minimum" : 1
        },
        "DeadLetterConfig" : {
          "$ref" : "#/definitions/DeadLetterConfig"
        },
        "OnPartialBatchItemFailure" : {
          "$ref" : "#/definitions/OnPartialBatchItemFailureStreams"
        },
        "MaximumBatchingWindowInSeconds" : {
          "type" : "integer",
          "maximum" : 300,
          "minimum" : 0
        },
        "MaximumRecordAgeInSeconds" : {
          "type" : "integer",
          "maximum" : 604800,
          "minimum" : -1
        },
        "MaximumRetryAttempts" : {
          "type" : "integer",
          "maximum" : 10000,
          "minimum" : -1
        },
        "ParallelizationFactor" : {
          "type" : "integer",
          "maximum" : 10,
          "minimum" : 1
        },
        "StartingPosition" : {
          "$ref" : "#/definitions/DynamoDBStreamStartPosition"
        }
      },
      "required" : [ "StartingPosition" ],
      "additionalProperties" : False
    },
    "PipeSourceKinesisStreamParameters" : {
      "type" : "object",
      "properties" : {
        "BatchSize" : {
          "type" : "integer",
          "maximum" : 10000,
          "minimum" : 1
        },
        "DeadLetterConfig" : {
          "$ref" : "#/definitions/DeadLetterConfig"
        },
        "OnPartialBatchItemFailure" : {
          "$ref" : "#/definitions/OnPartialBatchItemFailureStreams"
        },
        "MaximumBatchingWindowInSeconds" : {
          "type" : "integer",
          "maximum" : 300,
          "minimum" : 0
        },
        "MaximumRecordAgeInSeconds" : {
          "type" : "integer",
          "maximum" : 604800,
          "minimum" : -1
        },
        "MaximumRetryAttempts" : {
          "type" : "integer",
          "maximum" : 10000,
          "minimum" : -1
        },
        "ParallelizationFactor" : {
          "type" : "integer",
          "maximum" : 10,
          "minimum" : 1
        },
        "StartingPosition" : {
          "$ref" : "#/definitions/KinesisStreamStartPosition"
        },
        "StartingPositionTimestamp" : {
          "type" : "string",
          "format" : "date-time"
        }
      },
      "required" : [ "StartingPosition" ],
      "additionalProperties" : False
    },
    "PipeSourceManagedStreamingKafkaParameters" : {
      "type" : "object",
      "properties" : {
        "TopicName" : {
          "type" : "string",
          "maxLength" : 249,
          "minLength" : 1,
          "pattern" : "^[^.]([a-zA-Z0-9\\-_.]+)$"
        },
        "StartingPosition" : {
          "$ref" : "#/definitions/MSKStartPosition"
        },
        "BatchSize" : {
          "type" : "integer",
          "maximum" : 10000,
          "minimum" : 1
        },
        "MaximumBatchingWindowInSeconds" : {
          "type" : "integer",
          "maximum" : 300,
          "minimum" : 0
        },
        "ConsumerGroupID" : {
          "type" : "string",
          "maxLength" : 200,
          "minLength" : 1,
          "pattern" : "^[a-zA-Z0-9-\\/*:_+=.@-]*$"
        },
        "Credentials" : {
          "$ref" : "#/definitions/MSKAccessCredentials"
        }
      },
      "required" : [ "TopicName" ],
      "additionalProperties" : False
    },
    "PipeSourceParameters" : {
      "type" : "object",
      "properties" : {
        "FilterCriteria" : {
          "$ref" : "#/definitions/FilterCriteria"
        },
        "KinesisStreamParameters" : {
          "$ref" : "#/definitions/PipeSourceKinesisStreamParameters"
        },
        "DynamoDBStreamParameters" : {
          "$ref" : "#/definitions/PipeSourceDynamoDBStreamParameters"
        },
        "SqsQueueParameters" : {
          "$ref" : "#/definitions/PipeSourceSqsQueueParameters"
        },
        "ActiveMQBrokerParameters" : {
          "$ref" : "#/definitions/PipeSourceActiveMQBrokerParameters"
        },
        "RabbitMQBrokerParameters" : {
          "$ref" : "#/definitions/PipeSourceRabbitMQBrokerParameters"
        },
        "ManagedStreamingKafkaParameters" : {
          "$ref" : "#/definitions/PipeSourceManagedStreamingKafkaParameters"
        },
        "SelfManagedKafkaParameters" : {
          "$ref" : "#/definitions/PipeSourceSelfManagedKafkaParameters"
        }
      },
      "additionalProperties" : False
    },
    "PipeSourceRabbitMQBrokerParameters" : {
      "type" : "object",
      "properties" : {
        "Credentials" : {
          "$ref" : "#/definitions/MQBrokerAccessCredentials"
        },
        "QueueName" : {
          "type" : "string",
          "maxLength" : 1000,
          "minLength" : 1,
          "pattern" : "^[\\s\\S]*$"
        },
        "VirtualHost" : {
          "type" : "string",
          "maxLength" : 200,
          "minLength" : 1,
          "pattern" : "^[a-zA-Z0-9-\\/*:_+=.@-]*$"
        },
        "BatchSize" : {
          "type" : "integer",
          "maximum" : 10000,
          "minimum" : 1
        },
        "MaximumBatchingWindowInSeconds" : {
          "type" : "integer",
          "maximum" : 300,
          "minimum" : 0
        }
      },
      "required" : [ "Credentials", "QueueName" ],
      "additionalProperties" : False
    },
    "PipeSourceSelfManagedKafkaParameters" : {
      "type" : "object",
      "properties" : {
        "TopicName" : {
          "type" : "string",
          "maxLength" : 249,
          "minLength" : 1,
          "pattern" : "^[^.]([a-zA-Z0-9\\-_.]+)$"
        },
        "StartingPosition" : {
          "$ref" : "#/definitions/SelfManagedKafkaStartPosition"
        },
        "AdditionalBootstrapServers" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 300,
            "minLength" : 1,
            "pattern" : "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9]):[0-9]{1,5}$"
          },
          "maxItems" : 2,
          "minItems" : 0
        },
        "BatchSize" : {
          "type" : "integer",
          "maximum" : 10000,
          "minimum" : 1
        },
        "MaximumBatchingWindowInSeconds" : {
          "type" : "integer",
          "maximum" : 300,
          "minimum" : 0
        },
        "ConsumerGroupID" : {
          "type" : "string",
          "maxLength" : 200,
          "minLength" : 1,
          "pattern" : "^[a-zA-Z0-9-\\/*:_+=.@-]*$"
        },
        "Credentials" : {
          "$ref" : "#/definitions/SelfManagedKafkaAccessConfigurationCredentials"
        },
        "ServerRootCaCertificate" : {
          "type" : "string",
          "maxLength" : 1600,
          "minLength" : 1,
          "pattern" : "^(^arn:aws([a-z]|\\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1}):(\\d{12}):secret:.+)$",
          "description" : "Optional SecretManager ARN which stores the database credentials"
        },
        "Vpc" : {
          "$ref" : "#/definitions/SelfManagedKafkaAccessConfigurationVpc"
        }
      },
      "required" : [ "TopicName" ],
      "additionalProperties" : False
    },
    "PipeSourceSqsQueueParameters" : {
      "type" : "object",
      "properties" : {
        "BatchSize" : {
          "type" : "integer",
          "maximum" : 10000,
          "minimum" : 1
        },
        "MaximumBatchingWindowInSeconds" : {
          "type" : "integer",
          "maximum" : 300,
          "minimum" : 0
        }
      },
      "additionalProperties" : False
    },
    "PipeState" : {
      "type" : "string",
      "enum" : [ "RUNNING", "STOPPED", "CREATING", "UPDATING", "DELETING", "STARTING", "STOPPING", "CREATE_FAILED", "UPDATE_FAILED", "START_FAILED", "STOP_FAILED", "DELETE_FAILED", "CREATE_ROLLBACK_FAILED", "DELETE_ROLLBACK_FAILED", "UPDATE_ROLLBACK_FAILED" ]
    },
    "PipeTargetBatchJobParameters" : {
      "type" : "object",
      "properties" : {
        "JobDefinition" : {
          "type" : "string"
        },
        "JobName" : {
          "type" : "string"
        },
        "ArrayProperties" : {
          "$ref" : "#/definitions/BatchArrayProperties"
        },
        "RetryStrategy" : {
          "$ref" : "#/definitions/BatchRetryStrategy"
        },
        "ContainerOverrides" : {
          "$ref" : "#/definitions/BatchContainerOverrides"
        },
        "DependsOn" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/BatchJobDependency"
          },
          "maxItems" : 20,
          "minItems" : 0
        },
        "Parameters" : {
          "$ref" : "#/definitions/BatchParametersMap"
        }
      },
      "required" : [ "JobDefinition", "JobName" ],
      "additionalProperties" : False
    },
    "PipeTargetCloudWatchLogsParameters" : {
      "type" : "object",
      "properties" : {
        "LogStreamName" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1
        },
        "Timestamp" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "pattern" : "^\\$(\\.[\\w_-]+(\\[(\\d+|\\*)\\])*)*$"
        }
      },
      "additionalProperties" : False
    },
    "PipeTargetEcsTaskParameters" : {
      "type" : "object",
      "properties" : {
        "TaskDefinitionArn" : {
          "type" : "string",
          "maxLength" : 1600,
          "minLength" : 1,
          "pattern" : "^arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\\-]+):([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1})?:(\\d{12})?:(.+)|(\\$(\\.[\\w/_-]+(\\[(\\d+|\\*)\\])*)*)$"
        },
        "TaskCount" : {
          "type" : "integer",
          "minimum" : 1
        },
        "LaunchType" : {
          "$ref" : "#/definitions/LaunchType"
        },
        "NetworkConfiguration" : {
          "$ref" : "#/definitions/NetworkConfiguration"
        },
        "PlatformVersion" : {
          "type" : "string"
        },
        "Group" : {
          "type" : "string"
        },
        "CapacityProviderStrategy" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/CapacityProviderStrategyItem"
          },
          "maxItems" : 6,
          "minItems" : 0
        },
        "EnableECSManagedTags" : {
          "type" : "boolean",
          "default" : False
        },
        "EnableExecuteCommand" : {
          "type" : "boolean",
          "default" : False
        },
        "PlacementConstraints" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/PlacementConstraint"
          },
          "maxItems" : 10,
          "minItems" : 0
        },
        "PlacementStrategy" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/PlacementStrategy"
          },
          "maxItems" : 5,
          "minItems" : 0
        },
        "PropagateTags" : {
          "$ref" : "#/definitions/PropagateTags"
        },
        "ReferenceId" : {
          "type" : "string",
          "maxLength" : 1024,
          "minLength" : 0
        },
        "Overrides" : {
          "$ref" : "#/definitions/EcsTaskOverride"
        },
        "Tags" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/Tag"
          }
        }
      },
      "required" : [ "TaskDefinitionArn" ],
      "additionalProperties" : False
    },
    "PipeTargetEventBridgeEventBusParameters" : {
      "type" : "object",
      "properties" : {
        "EndpointId" : {
          "type" : "string",
          "maxLength" : 50,
          "minLength" : 1,
          "pattern" : "^[A-Za-z0-9\\-]+[\\.][A-Za-z0-9\\-]+$"
        },
        "DetailType" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1
        },
        "Source" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "pattern" : "(?=[/\\.\\-_A-Za-z0-9]+)((?!aws\\.).*)|(\\$(\\.[\\w/_-]+(\\[(\\d+|\\*)\\])*)*)"
        },
        "Resources" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 1600,
            "minLength" : 1,
            "pattern" : "^arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\\-]+):([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1})?:(\\d{12})?:(.+)|(\\$(\\.[\\w/_-]+(\\[(\\d+|\\*)\\])*)*)$"
          },
          "maxItems" : 10,
          "minItems" : 0
        },
        "Time" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "pattern" : "^\\$(\\.[\\w/_-]+(\\[(\\d+|\\*)\\])*)*$"
        }
      },
      "additionalProperties" : False
    },
    "PipeTargetHttpParameters" : {
      "type" : "object",
      "properties" : {
        "PathParameterValues" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "pattern" : "^(?!\\s*$).+|(\\$(\\.[\\w/_-]+(\\[(\\d+|\\*)\\])*)*)$"
          }
        },
        "HeaderParameters" : {
          "$ref" : "#/definitions/HeaderParametersMap"
        },
        "QueryStringParameters" : {
          "$ref" : "#/definitions/QueryStringParametersMap"
        }
      },
      "additionalProperties" : False
    },
    "PipeTargetInvocationType" : {
      "type" : "string",
      "enum" : [ "REQUEST_RESPONSE", "FIRE_AND_FORGET" ]
    },
    "PipeTargetKinesisStreamParameters" : {
      "type" : "object",
      "properties" : {
        "PartitionKey" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "required" : [ "PartitionKey" ],
      "additionalProperties" : False
    },
    "PipeTargetLambdaFunctionParameters" : {
      "type" : "object",
      "properties" : {
        "InvocationType" : {
          "$ref" : "#/definitions/PipeTargetInvocationType"
        }
      },
      "additionalProperties" : False
    },
    "PipeTargetParameters" : {
      "type" : "object",
      "properties" : {
        "InputTemplate" : {
          "type" : "string",
          "maxLength" : 8192,
          "minLength" : 0
        },
        "LambdaFunctionParameters" : {
          "$ref" : "#/definitions/PipeTargetLambdaFunctionParameters"
        },
        "StepFunctionStateMachineParameters" : {
          "$ref" : "#/definitions/PipeTargetStateMachineParameters"
        },
        "KinesisStreamParameters" : {
          "$ref" : "#/definitions/PipeTargetKinesisStreamParameters"
        },
        "EcsTaskParameters" : {
          "$ref" : "#/definitions/PipeTargetEcsTaskParameters"
        },
        "BatchJobParameters" : {
          "$ref" : "#/definitions/PipeTargetBatchJobParameters"
        },
        "SqsQueueParameters" : {
          "$ref" : "#/definitions/PipeTargetSqsQueueParameters"
        },
        "HttpParameters" : {
          "$ref" : "#/definitions/PipeTargetHttpParameters"
        },
        "RedshiftDataParameters" : {
          "$ref" : "#/definitions/PipeTargetRedshiftDataParameters"
        },
        "SageMakerPipelineParameters" : {
          "$ref" : "#/definitions/PipeTargetSageMakerPipelineParameters"
        },
        "EventBridgeEventBusParameters" : {
          "$ref" : "#/definitions/PipeTargetEventBridgeEventBusParameters"
        },
        "CloudWatchLogsParameters" : {
          "$ref" : "#/definitions/PipeTargetCloudWatchLogsParameters"
        },
        "TimestreamParameters" : {
          "$ref" : "#/definitions/PipeTargetTimestreamParameters"
        }
      },
      "additionalProperties" : False
    },
    "PipeTargetRedshiftDataParameters" : {
      "type" : "object",
      "properties" : {
        "SecretManagerArn" : {
          "type" : "string",
          "maxLength" : 1600,
          "minLength" : 1,
          "pattern" : "^(^arn:aws([a-z]|\\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1}):(\\d{12}):secret:.+)|(\\$(\\.[\\w/_-]+(\\[(\\d+|\\*)\\])*)*)$",
          "description" : "Optional SecretManager ARN which stores the database credentials"
        },
        "Database" : {
          "type" : "string",
          "maxLength" : 64,
          "minLength" : 1,
          "description" : "Redshift Database"
        },
        "DbUser" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "description" : "Database user name"
        },
        "StatementName" : {
          "type" : "string",
          "maxLength" : 500,
          "minLength" : 1,
          "description" : "A name for Redshift DataAPI statement which can be used as filter of ListStatement."
        },
        "WithEvent" : {
          "type" : "boolean",
          "default" : False
        },
        "Sqls" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 100000,
            "minLength" : 1,
            "description" : "A single Redshift SQL"
          },
          "maxItems" : 40,
          "minItems" : 1,
          "description" : "A list of SQLs."
        }
      },
      "required" : [ "Database", "Sqls" ],
      "additionalProperties" : False
    },
    "PipeTargetSageMakerPipelineParameters" : {
      "type" : "object",
      "properties" : {
        "PipelineParameterList" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/SageMakerPipelineParameter"
          },
          "maxItems" : 200,
          "minItems" : 0
        }
      },
      "additionalProperties" : False
    },
    "PipeTargetSqsQueueParameters" : {
      "type" : "object",
      "properties" : {
        "MessageGroupId" : {
          "type" : "string",
          "maxLength" : 100,
          "minLength" : 0
        },
        "MessageDeduplicationId" : {
          "type" : "string",
          "maxLength" : 100,
          "minLength" : 0
        }
      },
      "additionalProperties" : False
    },
    "PipeTargetStateMachineParameters" : {
      "type" : "object",
      "properties" : {
        "InvocationType" : {
          "$ref" : "#/definitions/PipeTargetInvocationType"
        }
      },
      "additionalProperties" : False
    },
    "PipeTargetTimestreamParameters" : {
      "type" : "object",
      "properties" : {
        "TimeValue" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1
        },
        "EpochTimeUnit" : {
          "$ref" : "#/definitions/EpochTimeUnit"
        },
        "TimeFieldType" : {
          "$ref" : "#/definitions/TimeFieldType"
        },
        "TimestampFormat" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1
        },
        "VersionValue" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1
        },
        "DimensionMappings" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/DimensionMapping"
          },
          "maxItems" : 128,
          "minItems" : 1
        },
        "SingleMeasureMappings" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/SingleMeasureMapping"
          },
          "maxItems" : 8192,
          "minItems" : 0
        },
        "MultiMeasureMappings" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/MultiMeasureMapping"
          },
          "maxItems" : 1024,
          "minItems" : 0
        }
      },
      "required" : [ "DimensionMappings", "TimeValue", "VersionValue" ],
      "additionalProperties" : False
    },
    "PlacementConstraint" : {
      "type" : "object",
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/PlacementConstraintType"
        },
        "Expression" : {
          "type" : "string",
          "maxLength" : 2000,
          "minLength" : 0
        }
      },
      "additionalProperties" : False
    },
    "PlacementConstraintType" : {
      "type" : "string",
      "enum" : [ "distinctInstance", "memberOf" ]
    },
    "PlacementStrategy" : {
      "type" : "object",
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/PlacementStrategyType"
        },
        "Field" : {
          "type" : "string",
          "maxLength" : 255,
          "minLength" : 0
        }
      },
      "additionalProperties" : False
    },
    "PlacementStrategyType" : {
      "type" : "string",
      "enum" : [ "random", "spread", "binpack" ]
    },
    "PropagateTags" : {
      "type" : "string",
      "enum" : [ "TASK_DEFINITION" ]
    },
    "QueryStringParametersMap" : {
      "type" : "object",
      "patternProperties" : {
        "^[^\\x00-\\x1F\\x7F]+|(\\$(\\.[\\w/_-]+(\\[(\\d+|\\*)\\])*)*)$" : {
          "type" : "string",
          "maxLength" : 512,
          "minLength" : 0,
          "pattern" : "^[^\\x00-\\x09\\x0B\\x0C\\x0E-\\x1F\\x7F]+|(\\$(\\.[\\w/_-]+(\\[(\\d+|\\*)\\])*)*)$"
        }
      },
      "additionalProperties" : False
    },
    "RequestedPipeState" : {
      "type" : "string",
      "enum" : [ "RUNNING", "STOPPED" ]
    },
    "S3LogDestination" : {
      "type" : "object",
      "properties" : {
        "BucketName" : {
          "type" : "string"
        },
        "Prefix" : {
          "type" : "string"
        },
        "BucketOwner" : {
          "type" : "string"
        },
        "OutputFormat" : {
          "$ref" : "#/definitions/S3OutputFormat"
        }
      },
      "additionalProperties" : False
    },
    "S3OutputFormat" : {
      "type" : "string",
      "enum" : [ "json", "plain", "w3c" ]
    },
    "SageMakerPipelineParameter" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9])*|(\\$(\\.[\\w/_-]+(\\[(\\d+|\\*)\\])*)*)$"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 1024,
          "minLength" : 0
        }
      },
      "required" : [ "Name", "Value" ],
      "additionalProperties" : False
    },
    "SelfManagedKafkaAccessConfigurationCredentials" : {
      "oneOf" : [ {
        "type" : "object",
        "title" : "BasicAuth",
        "properties" : {
          "BasicAuth" : {
            "type" : "string",
            "maxLength" : 1600,
            "minLength" : 1,
            "pattern" : "^(^arn:aws([a-z]|\\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1}):(\\d{12}):secret:.+)$",
            "description" : "Optional SecretManager ARN which stores the database credentials"
          }
        },
        "required" : [ "BasicAuth" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "SaslScram512Auth",
        "properties" : {
          "SaslScram512Auth" : {
            "type" : "string",
            "maxLength" : 1600,
            "minLength" : 1,
            "pattern" : "^(^arn:aws([a-z]|\\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1}):(\\d{12}):secret:.+)$",
            "description" : "Optional SecretManager ARN which stores the database credentials"
          }
        },
        "required" : [ "SaslScram512Auth" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "SaslScram256Auth",
        "properties" : {
          "SaslScram256Auth" : {
            "type" : "string",
            "maxLength" : 1600,
            "minLength" : 1,
            "pattern" : "^(^arn:aws([a-z]|\\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1}):(\\d{12}):secret:.+)$",
            "description" : "Optional SecretManager ARN which stores the database credentials"
          }
        },
        "required" : [ "SaslScram256Auth" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "ClientCertificateTlsAuth",
        "properties" : {
          "ClientCertificateTlsAuth" : {
            "type" : "string",
            "maxLength" : 1600,
            "minLength" : 1,
            "pattern" : "^(^arn:aws([a-z]|\\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1}):(\\d{12}):secret:.+)$",
            "description" : "Optional SecretManager ARN which stores the database credentials"
          }
        },
        "required" : [ "ClientCertificateTlsAuth" ],
        "additionalProperties" : False
      } ]
    },
    "SelfManagedKafkaAccessConfigurationVpc" : {
      "type" : "object",
      "properties" : {
        "Subnets" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 1024,
            "minLength" : 1,
            "pattern" : "^subnet-[0-9a-z]*$"
          },
          "maxItems" : 16,
          "minItems" : 0,
          "description" : "List of SubnetId."
        },
        "SecurityGroup" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 1024,
            "minLength" : 1,
            "pattern" : "^sg-[0-9a-zA-Z]*$"
          },
          "maxItems" : 5,
          "minItems" : 0,
          "description" : "List of SecurityGroupId."
        }
      },
      "additionalProperties" : False
    },
    "SelfManagedKafkaStartPosition" : {
      "type" : "string",
      "enum" : [ "TRIM_HORIZON", "LATEST" ]
    },
    "SingleMeasureMapping" : {
      "type" : "object",
      "properties" : {
        "MeasureValue" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 1
        },
        "MeasureValueType" : {
          "$ref" : "#/definitions/MeasureValueType"
        },
        "MeasureName" : {
          "type" : "string",
          "maxLength" : 1024,
          "minLength" : 1
        }
      },
      "required" : [ "MeasureName", "MeasureValue", "MeasureValueType" ],
      "additionalProperties" : False
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "TagMap" : {
      "type" : "object",
      "maxProperties" : 50,
      "minProperties" : 1,
      "patternProperties" : {
        ".+" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "additionalProperties" : False
    },
    "TimeFieldType" : {
      "type" : "string",
      "enum" : [ "EPOCH", "TIMESTAMP_FORMAT" ]
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "maxLength" : 1600,
      "minLength" : 1,
      "pattern" : "^arn:aws([a-z]|\\-)*:([a-zA-Z0-9\\-]+):([a-z]|\\d|\\-)*:([0-9]{12})?:(.+)$"
    },
    "CreationTime" : {
      "type" : "string",
      "format" : "date-time"
    },
    "CurrentState" : {
      "$ref" : "#/definitions/PipeState"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 512,
      "minLength" : 0,
      "pattern" : "^.*$"
    },
    "DesiredState" : {
      "$ref" : "#/definitions/RequestedPipeState"
    },
    "Enrichment" : {
      "type" : "string",
      "maxLength" : 1600,
      "minLength" : 0,
      "pattern" : "^$|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\\-]+):([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1})?:(\\d{12})?:(.+)$"
    },
    "EnrichmentParameters" : {
      "$ref" : "#/definitions/PipeEnrichmentParameters"
    },
    "KmsKeyIdentifier" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 0
    },
    "LastModifiedTime" : {
      "type" : "string",
      "format" : "date-time"
    },
    "LogConfiguration" : {
      "$ref" : "#/definitions/PipeLogConfiguration"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 64,
      "minLength" : 1,
      "pattern" : "^[\\.\\-_A-Za-z0-9]+$"
    },
    "RoleArn" : {
      "type" : "string",
      "maxLength" : 1600,
      "minLength" : 1,
      "pattern" : "^arn:(aws[a-zA-Z-]*)?:iam::\\d{12}:role/?[a-zA-Z0-9+=,.@\\-_/]+$"
    },
    "Source" : {
      "type" : "string",
      "maxLength" : 1600,
      "minLength" : 1,
      "pattern" : "^smk://(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9]):[0-9]{1,5}|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\\-]+):([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1})?:(\\d{12})?:(.+)$"
    },
    "SourceParameters" : {
      "$ref" : "#/definitions/PipeSourceParameters"
    },
    "StateReason" : {
      "type" : "string",
      "maxLength" : 512,
      "minLength" : 0,
      "pattern" : "^.*$"
    },
    "Tags" : {
      "$ref" : "#/definitions/TagMap"
    },
    "Target" : {
      "type" : "string",
      "maxLength" : 1600,
      "minLength" : 1,
      "pattern" : "^arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\\-]+):([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\\d{1})?:(\\d{12})?:(.+)$"
    },
    "TargetParameters" : {
      "$ref" : "#/definitions/PipeTargetParameters"
    }
  },
  "required" : [ "RoleArn", "Source", "Target" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreationTime", "/properties/CurrentState", "/properties/LastModifiedTime", "/properties/StateReason" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Source", "/properties/SourceParameters/DynamoDBStreamParameters/StartingPosition", "/properties/SourceParameters/KinesisStreamParameters/StartingPosition", "/properties/SourceParameters/KinesisStreamParameters/StartingPositionTimestamp", "/properties/SourceParameters/ActiveMQBrokerParameters/QueueName", "/properties/SourceParameters/RabbitMQBrokerParameters/QueueName", "/properties/SourceParameters/RabbitMQBrokerParameters/VirtualHost", "/properties/SourceParameters/ManagedStreamingKafkaParameters/TopicName", "/properties/SourceParameters/ManagedStreamingKafkaParameters/StartingPosition", "/properties/SourceParameters/ManagedStreamingKafkaParameters/ConsumerGroupID", "/properties/SourceParameters/SelfManagedKafkaParameters/TopicName", "/properties/SourceParameters/SelfManagedKafkaParameters/StartingPosition", "/properties/SourceParameters/SelfManagedKafkaParameters/AdditionalBootstrapServers", "/properties/SourceParameters/SelfManagedKafkaParameters/ConsumerGroupID" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "writeOnlyProperties" : [ "/properties/TargetParameters", "/properties/SourceParameters" ],
  "additionalIdentifiers" : [ [ "/properties/Arn" ] ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "pipes:TagResource", "pipes:UntagResource", "pipes:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "pipes:CreatePipe", "pipes:DescribePipe", "pipes:TagResource", "iam:PassRole", "logs:PutResourcePolicy", "logs:DescribeResourcePolicies", "logs:DescribeLogGroups", "iam:CreateServiceLinkedRole", "logs:CreateLogDelivery", "logs:GetLogDelivery", "logs:ListLogDeliveries", "s3:PutBucketPolicy", "s3:GetBucketPolicy", "firehose:TagDeliveryStream", "kms:DescribeKey", "kms:Decrypt", "kms:GenerateDataKey" ]
    },
    "read" : {
      "permissions" : [ "pipes:DescribePipe", "kms:Decrypt" ]
    },
    "update" : {
      "permissions" : [ "pipes:UpdatePipe", "pipes:TagResource", "pipes:UntagResource", "pipes:DescribePipe", "iam:PassRole", "logs:PutResourcePolicy", "logs:DescribeResourcePolicies", "logs:DescribeLogGroups", "iam:CreateServiceLinkedRole", "logs:CreateLogDelivery", "logs:UpdateLogDelivery", "logs:DeleteLogDelivery", "logs:GetLogDelivery", "logs:ListLogDeliveries", "s3:PutBucketPolicy", "s3:GetBucketPolicy", "firehose:TagDeliveryStream", "kms:DescribeKey", "kms:Decrypt", "kms:GenerateDataKey" ]
    },
    "delete" : {
      "permissions" : [ "pipes:DeletePipe", "pipes:DescribePipe", "pipes:UntagResource", "logs:CreateLogDelivery", "logs:UpdateLogDelivery", "logs:DeleteLogDelivery", "logs:GetLogDelivery", "logs:ListLogDeliveries", "kms:DescribeKey", "kms:Decrypt", "kms:GenerateDataKey" ]
    },
    "list" : {
      "permissions" : [ "pipes:ListPipes" ]
    }
  },
  "additionalProperties" : False
}