SCHEMA = {
  "typeName" : "AWS::AppRunner::VpcConnector",
  "description" : "The AWS::AppRunner::VpcConnector resource specifies an App Runner VpcConnector.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-apprunner.git",
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "VpcConnectorName" : {
      "description" : "A name for the VPC connector. If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.",
      "type" : "string",
      "minLength" : 4,
      "maxLength" : 40,
      "pattern" : "^[A-Za-z0-9][A-Za-z0-9-\\\\_]{3,39}$"
    },
    "VpcConnectorArn" : {
      "description" : "The Amazon Resource Name (ARN) of this VPC connector.",
      "type" : "string",
      "minLength" : 44,
      "maxLength" : 1011,
      "pattern" : "arn:aws(-[\\w]+)*:[a-z0-9-\\\\.]{0,63}:[a-z0-9-\\\\.]{0,63}:[0-9]{12}:(\\w|\\/|-){1,1011}"
    },
    "VpcConnectorRevision" : {
      "description" : "The revision of this VPC connector. It's unique among all the active connectors (\"Status\": \"ACTIVE\") that share the same Name.",
      "type" : "integer"
    },
    "Subnets" : {
      "description" : "A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "minItems" : 1,
      "items" : {
        "type" : "string"
      }
    },
    "SecurityGroups" : {
      "description" : "A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "Tags" : {
      "description" : "A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
  },
  "additionalProperties" : False,
  "required" : [ "Subnets" ],
  "createOnlyProperties" : [ "/properties/VpcConnectorName", "/properties/Subnets", "/properties/SecurityGroups", "/properties/Tags" ],
  "readOnlyProperties" : [ "/properties/VpcConnectorArn", "/properties/VpcConnectorRevision" ],
  "writeOnlyProperties" : [ "/properties/Tags" ],
  "primaryIdentifier" : [ "/properties/VpcConnectorArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:CreateServiceLinkedRole", "apprunner:CreateVpcConnector", "apprunner:DescribeVpcConnector", "apprunner:TagResource", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups" ]
    },
    "read" : {
      "permissions" : [ "apprunner:DescribeVpcConnector" ]
    },
    "delete" : {
      "permissions" : [ "apprunner:DeleteVpcConnector" ]
    },
    "list" : {
      "permissions" : [ "apprunner:ListVpcConnectors" ]
    }
  }
}