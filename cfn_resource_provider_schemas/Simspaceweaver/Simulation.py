SCHEMA = {
  "typeName" : "AWS::SimSpaceWeaver::Simulation",
  "description" : "AWS::SimSpaceWeaver::Simulation resource creates an AWS Simulation.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "S3Location" : {
      "type" : "object",
      "properties" : {
        "BucketName" : {
          "description" : "The Schema S3 bucket name.",
          "type" : "string",
          "minLength" : 3,
          "maxLength" : 63,
          "pattern" : "[a-zA-Z0-9_\\-]{3,63}$"
        },
        "ObjectKey" : {
          "description" : "This is the schema S3 object key, which includes the full path of \"folders\" from the bucket root to the schema.",
          "type" : "string",
          "minLength" : 3,
          "maxLength" : 255
        }
      },
      "required" : [ "BucketName", "ObjectKey" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Name" : {
      "description" : "The name of the simulation.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048,
      "pattern" : "[a-zA-Z0-9_\\-]{1,2048}$"
    },
    "RoleArn" : {
      "description" : "Role ARN.",
      "type" : "string"
    },
    "SchemaS3Location" : {
      "$ref" : "#/definitions/S3Location"
    },
    "DescribePayload" : {
      "description" : "Json object with all simulation details",
      "type" : "string"
    },
    "MaximumDuration" : {
      "description" : "The maximum running time of the simulation.",
      "type" : "string",
      "minLength" : 2,
      "maxLength" : 6
    },
    "SnapshotS3Location" : {
      "$ref" : "#/definitions/S3Location"
    }
  },
  "required" : [ "Name", "RoleArn" ],
  "oneOf" : [ {
    "required" : [ "SchemaS3Location" ]
  }, {
    "required" : [ "SnapshotS3Location" ]
  } ],
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/DescribePayload" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/RoleArn", "/properties/SchemaS3Location", "/properties/SnapshotS3Location", "/properties/MaximumDuration" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "propertyTransform" : {
    "properties/MaximumDuration" : "$uppercase(MaximumDuration)"
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "simspaceweaver:StartSimulation", "simspaceweaver:DescribeSimulation", "iam:GetRole", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "simspaceweaver:DescribeSimulation" ]
    },
    "update" : {
      "permissions" : [ "simspaceweaver:StartSimulation", "simspaceweaver:StopSimulation", "simspaceweaver:DeleteSimulation", "simspaceweaver:DescribeSimulation" ]
    },
    "delete" : {
      "permissions" : [ "simspaceweaver:StopSimulation", "simspaceweaver:DeleteSimulation", "simspaceweaver:DescribeSimulation" ]
    },
    "list" : {
      "permissions" : [ "simspaceweaver:ListSimulations" ]
    }
  }
}