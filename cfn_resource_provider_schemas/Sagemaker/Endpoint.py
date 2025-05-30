SCHEMA = {
  "typeName" : "AWS::SageMaker::Endpoint",
  "description" : "Resource Type definition for AWS::SageMaker::Endpoint",
  "additionalProperties" : False,
  "properties" : {
    "DeploymentConfig" : {
      "$ref" : "#/definitions/DeploymentConfig",
      "description" : "Specifies deployment configuration for updating the SageMaker endpoint. Includes rollback and update policies."
    },
    "EndpointArn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the endpoint."
    },
    "EndpointConfigName" : {
      "type" : "string",
      "description" : "The name of the endpoint configuration for the SageMaker endpoint. This is a required property."
    },
    "EndpointName" : {
      "type" : "string",
      "description" : "The name of the SageMaker endpoint. This name must be unique within an AWS Region."
    },
    "ExcludeRetainedVariantProperties" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/VariantProperty"
      },
      "description" : "Specifies a list of variant properties that you want to exclude when updating an endpoint."
    },
    "RetainAllVariantProperties" : {
      "type" : "boolean",
      "description" : "When set to True, retains all variant properties for an endpoint when it is updated."
    },
    "RetainDeploymentConfig" : {
      "type" : "boolean",
      "description" : "When set to True, retains the deployment configuration during endpoint updates."
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "description" : "An array of key-value pairs to apply to this resource."
    }
  },
  "definitions" : {
    "Alarm" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AlarmName" : {
          "type" : "string",
          "description" : "The name of the CloudWatch alarm."
        }
      },
      "required" : [ "AlarmName" ]
    },
    "AutoRollbackConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Alarms" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/Alarm"
          },
          "description" : "List of CloudWatch alarms to monitor during the deployment. If any alarm goes off, the deployment is rolled back."
        }
      },
      "required" : [ "Alarms" ]
    },
    "BlueGreenUpdatePolicy" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MaximumExecutionTimeoutInSeconds" : {
          "type" : "integer",
          "description" : "The maximum time allowed for the blue/green update, in seconds."
        },
        "TerminationWaitInSeconds" : {
          "type" : "integer",
          "description" : "The wait time before terminating the old endpoint during a blue/green deployment."
        },
        "TrafficRoutingConfiguration" : {
          "$ref" : "#/definitions/TrafficRoutingConfig",
          "description" : "The traffic routing configuration for the blue/green deployment."
        }
      },
      "required" : [ "TrafficRoutingConfiguration" ]
    },
    "CapacitySize" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Type" : {
          "type" : "string",
          "description" : "Specifies whether the `Value` is an instance count or a capacity unit."
        },
        "Value" : {
          "type" : "integer",
          "description" : "The value representing either the number of instances or the number of capacity units."
        }
      },
      "required" : [ "Type", "Value" ]
    },
    "DeploymentConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AutoRollbackConfiguration" : {
          "$ref" : "#/definitions/AutoRollbackConfig",
          "description" : "Configuration for automatic rollback if an error occurs during deployment."
        },
        "BlueGreenUpdatePolicy" : {
          "$ref" : "#/definitions/BlueGreenUpdatePolicy",
          "description" : "Configuration for blue-green update deployment policies."
        },
        "RollingUpdatePolicy" : {
          "$ref" : "#/definitions/RollingUpdatePolicy",
          "description" : "Configuration for rolling update deployment policies."
        }
      }
    },
    "RollingUpdatePolicy" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MaximumBatchSize" : {
          "$ref" : "#/definitions/CapacitySize",
          "description" : "Specifies the maximum batch size for each rolling update."
        },
        "MaximumExecutionTimeoutInSeconds" : {
          "type" : "integer",
          "description" : "The maximum time allowed for the rolling update, in seconds."
        },
        "RollbackMaximumBatchSize" : {
          "$ref" : "#/definitions/CapacitySize",
          "description" : "The maximum batch size for rollback during an update failure."
        },
        "WaitIntervalInSeconds" : {
          "type" : "integer",
          "description" : "The time to wait between steps during the rolling update, in seconds."
        }
      },
      "required" : [ "MaximumBatchSize", "WaitIntervalInSeconds" ]
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key of the tag."
        },
        "Value" : {
          "type" : "string",
          "description" : "The value of the tag."
        }
      },
      "required" : [ "Value", "Key" ]
    },
    "TrafficRoutingConfig" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CanarySize" : {
          "$ref" : "#/definitions/CapacitySize",
          "description" : "Specifies the size of the canary traffic in a canary deployment."
        },
        "LinearStepSize" : {
          "$ref" : "#/definitions/CapacitySize",
          "description" : "Specifies the step size for linear traffic routing."
        },
        "Type" : {
          "type" : "string",
          "description" : "Specifies the type of traffic routing (e.g., 'AllAtOnce', 'Canary', 'Linear')."
        },
        "WaitIntervalInSeconds" : {
          "type" : "integer",
          "description" : "Specifies the wait interval between traffic shifts, in seconds."
        }
      },
      "required" : [ "Type" ]
    },
    "VariantProperty" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "VariantPropertyType" : {
          "type" : "string",
          "description" : "The type of variant property (e.g., 'DesiredInstanceCount', 'DesiredWeight', 'DataCaptureConfig')."
        }
      }
    }
  },
  "required" : [ "EndpointConfigName" ],
  "createOnlyProperties" : [ "/properties/EndpointName" ],
  "primaryIdentifier" : [ "/properties/EndpointArn" ],
  "readOnlyProperties" : [ "/properties/EndpointArn", "/properties/EndpointName" ],
  "writeOnlyProperties" : [ "/properties/ExcludeRetainedVariantProperties", "/properties/RetainAllVariantProperties", "/properties/RetainDeploymentConfig" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "sagemaker:CreateEndpoint", "sagemaker:DescribeEndpoint", "sagemaker:AddTags" ]
    },
    "read" : {
      "permissions" : [ "sagemaker:DescribeEndpoint", "sagemaker:ListTags" ]
    },
    "update" : {
      "permissions" : [ "sagemaker:UpdateEndpoint", "sagemaker:DescribeEndpoint", "sagemaker:AddTags", "sagemaker:DeleteTags" ]
    },
    "delete" : {
      "permissions" : [ "sagemaker:DeleteEndpoint", "sagemaker:DescribeEndpoint" ]
    },
    "list" : {
      "permissions" : [ "sagemaker:ListEndpoints" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "sagemaker:AddTags", "sagemaker:DeleteTags", "sagemaker:ListTags" ]
  }
}