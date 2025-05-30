SCHEMA = {
  "typeName" : "AWS::AppFlow::Connector",
  "description" : "Resource schema for AWS::AppFlow::Connector",
  "sourceUrl" : "https://docs.aws.amazon.com/appflow/latest/userguide/what-is-appflow.html",
  "additionalProperties" : False,
  "properties" : {
    "ConnectorLabel" : {
      "description" : " The name of the connector. The name is unique for each ConnectorRegistration in your AWS account.",
      "type" : "string",
      "pattern" : "[a-zA-Z0-9][\\w!@#.-]+",
      "maxLength" : 512
    },
    "ConnectorArn" : {
      "description" : " The arn of the connector. The arn is unique for each ConnectorRegistration in your AWS account.",
      "type" : "string",
      "pattern" : "arn:.*:appflow:.*:[0-9]+:.*",
      "maxLength" : 512
    },
    "ConnectorProvisioningType" : {
      "description" : "The provisioning type of the connector. Currently the only supported value is LAMBDA. ",
      "type" : "string",
      "pattern" : "[a-zA-Z0-9][\\w!@#.-]+",
      "maxLength" : 256,
      "minLength" : 1
    },
    "ConnectorProvisioningConfig" : {
      "description" : "Contains information about the configuration of the connector being registered.",
      "$ref" : "#/definitions/ConnectorProvisioningConfig"
    },
    "Description" : {
      "description" : "A description about the connector that's being registered.",
      "type" : "string",
      "pattern" : "[\\s\\w/!@#+=.-]*",
      "maxLength" : 2048
    }
  },
  "definitions" : {
    "ConnectorProvisioningConfig" : {
      "description" : "Contains information about the configuration of the connector being registered.",
      "type" : "object",
      "properties" : {
        "Lambda" : {
          "description" : "Contains information about the configuration of the lambda which is being registered as the connector.",
          "$ref" : "#/definitions/LambdaConnectorProvisioningConfig"
        }
      },
      "additionalProperties" : False
    },
    "LambdaConnectorProvisioningConfig" : {
      "description" : "Contains information about the configuration of the lambda which is being registered as the connector.",
      "type" : "object",
      "properties" : {
        "LambdaArn" : {
          "description" : "Lambda ARN of the connector being registered.",
          "type" : "string",
          "pattern" : "arn:*:.*:.*:[0-9]+:.*",
          "maxLength" : 512
        }
      },
      "required" : [ "LambdaArn" ],
      "additionalProperties" : False
    }
  },
  "required" : [ "ConnectorProvisioningType", "ConnectorProvisioningConfig" ],
  "createOnlyProperties" : [ "/properties/ConnectorLabel" ],
  "readOnlyProperties" : [ "/properties/ConnectorArn" ],
  "primaryIdentifier" : [ "/properties/ConnectorLabel" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "appflow:RegisterConnector", "lambda:InvokeFunction" ]
    },
    "read" : {
      "permissions" : [ "appflow:DescribeConnector" ]
    },
    "delete" : {
      "permissions" : [ "appflow:UnRegisterConnector" ]
    },
    "list" : {
      "permissions" : [ "appflow:ListConnectors" ]
    },
    "update" : {
      "permissions" : [ "appflow:UpdateConnectorRegistration", "lambda:InvokeFunction" ]
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  }
}