SCHEMA = {
  "typeName" : "AWS::AutoScalingPlans::ScalingPlan",
  "description" : "Resource Type definition for AWS::AutoScalingPlans::ScalingPlan",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "ScalingPlanName" : {
      "type" : "string"
    },
    "ScalingPlanVersion" : {
      "type" : "string"
    },
    "ApplicationSource" : {
      "$ref" : "#/definitions/ApplicationSource"
    },
    "ScalingInstructions" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/ScalingInstruction"
      }
    }
  },
  "definitions" : {
    "ScalingInstruction" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DisableDynamicScaling" : {
          "type" : "boolean"
        },
        "ServiceNamespace" : {
          "type" : "string"
        },
        "PredictiveScalingMaxCapacityBehavior" : {
          "type" : "string"
        },
        "ScalableDimension" : {
          "type" : "string"
        },
        "ScalingPolicyUpdateBehavior" : {
          "type" : "string"
        },
        "MinCapacity" : {
          "type" : "integer"
        },
        "TargetTrackingConfigurations" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/TargetTrackingConfiguration"
          }
        },
        "PredictiveScalingMaxCapacityBuffer" : {
          "type" : "integer"
        },
        "CustomizedLoadMetricSpecification" : {
          "$ref" : "#/definitions/CustomizedLoadMetricSpecification"
        },
        "PredefinedLoadMetricSpecification" : {
          "$ref" : "#/definitions/PredefinedLoadMetricSpecification"
        },
        "ResourceId" : {
          "type" : "string"
        },
        "ScheduledActionBufferTime" : {
          "type" : "integer"
        },
        "MaxCapacity" : {
          "type" : "integer"
        },
        "PredictiveScalingMode" : {
          "type" : "string"
        }
      },
      "required" : [ "ResourceId", "ServiceNamespace", "ScalableDimension", "MinCapacity", "TargetTrackingConfigurations", "MaxCapacity" ]
    },
    "ApplicationSource" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CloudFormationStackARN" : {
          "type" : "string"
        },
        "TagFilters" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/TagFilter"
          }
        }
      }
    },
    "TargetTrackingConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ScaleOutCooldown" : {
          "type" : "integer"
        },
        "TargetValue" : {
          "type" : "number"
        },
        "PredefinedScalingMetricSpecification" : {
          "$ref" : "#/definitions/PredefinedScalingMetricSpecification"
        },
        "DisableScaleIn" : {
          "type" : "boolean"
        },
        "ScaleInCooldown" : {
          "type" : "integer"
        },
        "EstimatedInstanceWarmup" : {
          "type" : "integer"
        },
        "CustomizedScalingMetricSpecification" : {
          "$ref" : "#/definitions/CustomizedScalingMetricSpecification"
        }
      },
      "required" : [ "TargetValue" ]
    },
    "CustomizedLoadMetricSpecification" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MetricName" : {
          "type" : "string"
        },
        "Statistic" : {
          "type" : "string"
        },
        "Dimensions" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/MetricDimension"
          }
        },
        "Unit" : {
          "type" : "string"
        },
        "Namespace" : {
          "type" : "string"
        }
      },
      "required" : [ "MetricName", "Statistic", "Namespace" ]
    },
    "PredefinedLoadMetricSpecification" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "PredefinedLoadMetricType" : {
          "type" : "string"
        },
        "ResourceLabel" : {
          "type" : "string"
        }
      },
      "required" : [ "PredefinedLoadMetricType" ]
    },
    "TagFilter" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Values" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Key" ]
    },
    "PredefinedScalingMetricSpecification" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ResourceLabel" : {
          "type" : "string"
        },
        "PredefinedScalingMetricType" : {
          "type" : "string"
        }
      },
      "required" : [ "PredefinedScalingMetricType" ]
    },
    "CustomizedScalingMetricSpecification" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MetricName" : {
          "type" : "string"
        },
        "Statistic" : {
          "type" : "string"
        },
        "Dimensions" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/MetricDimension"
          }
        },
        "Unit" : {
          "type" : "string"
        },
        "Namespace" : {
          "type" : "string"
        }
      },
      "required" : [ "MetricName", "Statistic", "Namespace" ]
    },
    "MetricDimension" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Name" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Name" ]
    }
  },
  "required" : [ "ScalingInstructions", "ApplicationSource" ],
  "readOnlyProperties" : [ "/properties/ScalingPlanVersion", "/properties/ScalingPlanName", "/properties/Id" ],
  "primaryIdentifier" : [ "/properties/Id" ]
}