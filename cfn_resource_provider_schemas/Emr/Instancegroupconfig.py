SCHEMA = {
  "typeName" : "AWS::EMR::InstanceGroupConfig",
  "description" : "Resource Type definition for AWS::EMR::InstanceGroupConfig",
  "additionalProperties" : False,
  "properties" : {
    "JobFlowId" : {
      "type" : "string"
    },
    "AutoScalingPolicy" : {
      "$ref" : "#/definitions/AutoScalingPolicy"
    },
    "BidPrice" : {
      "type" : "string"
    },
    "InstanceCount" : {
      "type" : "integer"
    },
    "EbsConfiguration" : {
      "$ref" : "#/definitions/EbsConfiguration"
    },
    "InstanceRole" : {
      "type" : "string"
    },
    "CustomAmiId" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "Configurations" : {
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Configuration"
      }
    },
    "InstanceType" : {
      "type" : "string"
    },
    "Market" : {
      "type" : "string"
    },
    "Name" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "AutoScalingPolicy" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Rules" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/ScalingRule"
          }
        },
        "Constraints" : {
          "$ref" : "#/definitions/ScalingConstraints"
        }
      },
      "required" : [ "Constraints", "Rules" ]
    },
    "VolumeSpecification" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SizeInGB" : {
          "type" : "integer"
        },
        "Throughput" : {
          "type" : "integer"
        },
        "VolumeType" : {
          "type" : "string"
        },
        "Iops" : {
          "type" : "integer"
        }
      },
      "required" : [ "SizeInGB", "VolumeType" ]
    },
    "CloudWatchAlarmDefinition" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MetricName" : {
          "type" : "string"
        },
        "ComparisonOperator" : {
          "type" : "string"
        },
        "Statistic" : {
          "type" : "string"
        },
        "Dimensions" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/MetricDimension"
          }
        },
        "Period" : {
          "type" : "integer"
        },
        "EvaluationPeriods" : {
          "type" : "integer"
        },
        "Unit" : {
          "type" : "string"
        },
        "Namespace" : {
          "type" : "string"
        },
        "Threshold" : {
          "type" : "number"
        }
      },
      "required" : [ "MetricName", "ComparisonOperator", "Period", "Threshold" ]
    },
    "EbsConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "EbsBlockDeviceConfigs" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/EbsBlockDeviceConfig"
          }
        },
        "EbsOptimized" : {
          "type" : "boolean"
        }
      }
    },
    "Configuration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ConfigurationProperties" : {
          "type" : "object",
          "patternProperties" : {
            "[a-zA-Z0-9]+" : {
              "type" : "string"
            }
          }
        },
        "Configurations" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/Configuration"
          }
        },
        "Classification" : {
          "type" : "string"
        }
      }
    },
    "ScalingAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Market" : {
          "type" : "string"
        },
        "SimpleScalingPolicyConfiguration" : {
          "$ref" : "#/definitions/SimpleScalingPolicyConfiguration"
        }
      },
      "required" : [ "SimpleScalingPolicyConfiguration" ]
    },
    "SimpleScalingPolicyConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ScalingAdjustment" : {
          "type" : "integer"
        },
        "CoolDown" : {
          "type" : "integer"
        },
        "AdjustmentType" : {
          "type" : "string"
        }
      },
      "required" : [ "ScalingAdjustment" ]
    },
    "ScalingConstraints" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MinCapacity" : {
          "type" : "integer"
        },
        "MaxCapacity" : {
          "type" : "integer"
        }
      },
      "required" : [ "MinCapacity", "MaxCapacity" ]
    },
    "EbsBlockDeviceConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "VolumeSpecification" : {
          "$ref" : "#/definitions/VolumeSpecification"
        },
        "VolumesPerInstance" : {
          "type" : "integer"
        }
      },
      "required" : [ "VolumeSpecification" ]
    },
    "ScalingTrigger" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CloudWatchAlarmDefinition" : {
          "$ref" : "#/definitions/CloudWatchAlarmDefinition"
        }
      },
      "required" : [ "CloudWatchAlarmDefinition" ]
    },
    "ScalingRule" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Action" : {
          "$ref" : "#/definitions/ScalingAction"
        },
        "Description" : {
          "type" : "string"
        },
        "Trigger" : {
          "$ref" : "#/definitions/ScalingTrigger"
        },
        "Name" : {
          "type" : "string"
        }
      },
      "required" : [ "Action", "Trigger", "Name" ]
    },
    "MetricDimension" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "required" : [ "JobFlowId", "InstanceCount", "InstanceRole", "InstanceType" ],
  "createOnlyProperties" : [ "/properties/InstanceRole", "/properties/JobFlowId", "/properties/Name", "/properties/InstanceType", "/properties/CustomAmiId", "/properties/Configurations", "/properties/EbsConfiguration", "/properties/Market", "/properties/BidPrice" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}