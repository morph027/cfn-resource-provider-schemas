SCHEMA = {
  "typeName" : "AWS::MSK::Replicator",
  "description" : "Resource Type definition for AWS::MSK::Replicator",
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "kafka:UntagResource", "kafka:ListTagsForResource", "kafka:TagResource" ]
  },
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-msk-replicator.git",
  "properties" : {
    "ReplicatorArn" : {
      "description" : "Amazon Resource Name for the created replicator.",
      "type" : "string",
      "pattern" : "arn:(aws|aws-us-gov|aws-cn):kafka:.*"
    },
    "ReplicatorName" : {
      "description" : "The name of the replicator.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "^[0-9A-Za-z][0-9A-Za-z-]{0,}$"
    },
    "CurrentVersion" : {
      "description" : "The current version of the MSK replicator.",
      "type" : "string"
    },
    "Description" : {
      "description" : "A summary description of the replicator.",
      "type" : "string",
      "maxLength" : 1024
    },
    "KafkaClusters" : {
      "description" : "Specifies a list of Kafka clusters which are targets of the replicator.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "minItems" : 2,
      "maxItems" : 2,
      "items" : {
        "$ref" : "#/definitions/KafkaCluster"
      }
    },
    "ReplicationInfoList" : {
      "description" : "A list of replication configurations, where each configuration targets a given source cluster to target cluster replication flow.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "minItems" : 1,
      "maxItems" : 1,
      "items" : {
        "$ref" : "#/definitions/ReplicationInfo"
      }
    },
    "ServiceExecutionRoleArn" : {
      "description" : "The Amazon Resource Name (ARN) of the IAM role used by the replicator to access external resources.",
      "type" : "string",
      "pattern" : "arn:(aws|aws-us-gov|aws-cn):iam:.*"
    },
    "Tags" : {
      "description" : "A collection of tags associated with a resource",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ],
      "additionalProperties" : False
    },
    "TopicReplication" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TopicsToReplicate" : {
          "description" : "List of regular expression patterns indicating the topics to copy.",
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "minItems" : 1,
          "maxItems" : 100,
          "items" : {
            "type" : "string",
            "maxLength" : 249
          }
        },
        "TopicsToExclude" : {
          "description" : "List of regular expression patterns indicating the topics that should not be replicated.",
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "minItems" : 1,
          "maxItems" : 100,
          "items" : {
            "type" : "string",
            "maxLength" : 249
          }
        },
        "CopyTopicConfigurations" : {
          "description" : "Whether to periodically configure remote topics to match their corresponding upstream topics.",
          "type" : "boolean"
        },
        "CopyAccessControlListsForTopics" : {
          "description" : "Whether to periodically configure remote topic ACLs to match their corresponding upstream topics.",
          "type" : "boolean"
        },
        "DetectAndCopyNewTopics" : {
          "description" : "Whether to periodically check for new topics and partitions.",
          "type" : "boolean"
        },
        "StartingPosition" : {
          "description" : "Configuration for specifying the position in the topics to start replicating from.",
          "$ref" : "#/definitions/ReplicationStartingPosition"
        },
        "TopicNameConfiguration" : {
          "description" : "Configuration for specifying replicated topic names should be the same as their corresponding upstream topics or prefixed with source cluster alias.",
          "$ref" : "#/definitions/ReplicationTopicNameConfiguration"
        }
      },
      "required" : [ "TopicsToReplicate" ]
    },
    "ReplicationStartingPosition" : {
      "description" : "Configuration for specifying the position in the topics to start replicating from.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/ReplicationStartingPositionType"
        }
      },
      "required" : [ ]
    },
    "ReplicationStartingPositionType" : {
      "description" : "The type of replication starting position.",
      "type" : "string",
      "enum" : [ "LATEST", "EARLIEST" ]
    },
    "ReplicationTopicNameConfiguration" : {
      "description" : "Configuration for specifying replicated topic names should be the same as their corresponding upstream topics or prefixed with source cluster alias.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/ReplicationTopicNameConfigurationType"
        }
      },
      "required" : [ ]
    },
    "ReplicationTopicNameConfigurationType" : {
      "description" : "The type of replicated topic name.",
      "type" : "string",
      "enum" : [ "PREFIXED_WITH_SOURCE_CLUSTER_ALIAS", "IDENTICAL" ]
    },
    "ConsumerGroupReplication" : {
      "description" : "Configuration relating to consumer group replication.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ConsumerGroupsToReplicate" : {
          "description" : "List of regular expression patterns indicating the consumer groups to copy.",
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "minItems" : 0,
          "maxItems" : 100,
          "items" : {
            "type" : "string",
            "maxLength" : 256
          }
        },
        "ConsumerGroupsToExclude" : {
          "description" : "List of regular expression patterns indicating the consumer groups that should not be replicated.",
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "minItems" : 1,
          "maxItems" : 100,
          "items" : {
            "type" : "string",
            "maxLength" : 256
          }
        },
        "SynchroniseConsumerGroupOffsets" : {
          "description" : "Whether to periodically write the translated offsets to __consumer_offsets topic in target cluster.",
          "type" : "boolean"
        },
        "DetectAndCopyNewConsumerGroups" : {
          "description" : "Whether to periodically check for new consumer groups.",
          "type" : "boolean"
        }
      },
      "required" : [ "ConsumerGroupsToReplicate" ]
    },
    "ReplicationInfo" : {
      "description" : "Specifies configuration for replication between a source and target Kafka cluster.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SourceKafkaClusterArn" : {
          "description" : "Amazon Resource Name of the source Kafka cluster.",
          "type" : "string",
          "pattern" : "arn:(aws|aws-us-gov|aws-cn):kafka:.*"
        },
        "TargetKafkaClusterArn" : {
          "description" : "Amazon Resource Name of the target Kafka cluster.",
          "type" : "string",
          "pattern" : "arn:(aws|aws-us-gov|aws-cn):kafka:.*"
        },
        "TargetCompressionType" : {
          "description" : "The type of compression to use writing records to target Kafka cluster.",
          "type" : "string",
          "enum" : [ "NONE", "GZIP", "SNAPPY", "LZ4", "ZSTD" ]
        },
        "TopicReplication" : {
          "description" : "Configuration relating to topic replication.",
          "$ref" : "#/definitions/TopicReplication"
        },
        "ConsumerGroupReplication" : {
          "description" : "Configuration relating to consumer group replication.",
          "$ref" : "#/definitions/ConsumerGroupReplication"
        }
      },
      "required" : [ "SourceKafkaClusterArn", "TargetKafkaClusterArn", "TopicReplication", "ConsumerGroupReplication", "TargetCompressionType" ]
    },
    "AmazonMskCluster" : {
      "description" : "Details of an Amazon MSK cluster.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MskClusterArn" : {
          "description" : "The ARN of an Amazon MSK cluster.",
          "type" : "string",
          "pattern" : "arn:(aws|aws-us-gov|aws-cn):kafka:.*"
        }
      },
      "required" : [ "MskClusterArn" ]
    },
    "KafkaClusterClientVpcConfig" : {
      "description" : "Details of an Amazon VPC which has network connectivity to the Kafka cluster.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SecurityGroupIds" : {
          "description" : "The AWS security groups to associate with the elastic network interfaces in order to specify what the replicator has access to. If a security group is not specified, the default security group associated with the VPC is used.",
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "minItems" : 1,
          "maxItems" : 16,
          "items" : {
            "type" : "string"
          }
        },
        "SubnetIds" : {
          "description" : "The list of subnets to connect to in the virtual private cloud (VPC). AWS creates elastic network interfaces inside these subnets.",
          "type" : "array",
          "uniqueItems" : True,
          "insertionOrder" : False,
          "minItems" : 2,
          "maxItems" : 3,
          "items" : {
            "type" : "string"
          }
        }
      },
      "required" : [ "SubnetIds" ]
    },
    "KafkaCluster" : {
      "description" : "Details of a Kafka cluster for replication.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AmazonMskCluster" : {
          "description" : "Details of an Amazon MSK cluster. Exactly one of AmazonMskCluster is required.",
          "$ref" : "#/definitions/AmazonMskCluster"
        },
        "VpcConfig" : {
          "description" : "Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.",
          "$ref" : "#/definitions/KafkaClusterClientVpcConfig"
        }
      },
      "required" : [ "AmazonMskCluster", "VpcConfig" ]
    }
  },
  "required" : [ "ReplicatorName", "ReplicationInfoList", "KafkaClusters", "ServiceExecutionRoleArn" ],
  "primaryIdentifier" : [ "/properties/ReplicatorArn" ],
  "additionalIdentifiers" : [ [ "/properties/ReplicatorName" ] ],
  "readOnlyProperties" : [ "/properties/ReplicatorArn", "/properties/CurrentVersion" ],
  "createOnlyProperties" : [ "/properties/ReplicatorName", "/properties/Description", "/properties/KafkaClusters", "/properties/ServiceExecutionRoleArn", "/properties/ReplicationInfoList/*/SourceKafkaClusterArn", "/properties/ReplicationInfoList/*/TargetKafkaClusterArn", "/properties/ReplicationInfoList/*/TargetCompressionType", "/properties/ReplicationInfoList/*/TopicReplication/StartingPosition", "/properties/ReplicationInfoList/*/TopicReplication/TopicNameConfiguration" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateNetworkInterface", "ec2:DescribeSecurityGroups", "ec2:DescribeSubnets", "ec2:DescribeVpcs", "iam:CreateServiceLinkedRole", "iam:PassRole", "kafka:CreateReplicator", "kafka:CreateReplicatorReference", "kafka:DescribeClusterV2", "kafka:DescribeReplicator", "kafka:GetBootstrapBrokers", "kafka:ListTagsForResource", "kafka:TagResource" ]
    },
    "read" : {
      "permissions" : [ "kafka:DescribeReplicator", "kafka:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "kafka:DescribeReplicator", "kafka:ListTagsForResource", "kafka:TagResource", "kafka:UntagResource", "kafka:UpdateReplicationInfo" ]
    },
    "delete" : {
      "permissions" : [ "kafka:DeleteReplicator", "kafka:DescribeReplicator", "kafka:ListTagsForResource", "kafka:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "kafka:ListReplicators" ]
    }
  }
}