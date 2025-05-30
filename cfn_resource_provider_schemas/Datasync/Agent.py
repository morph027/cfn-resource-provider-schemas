SCHEMA = {
  "typeName" : "AWS::DataSync::Agent",
  "description" : "Resource schema for AWS::DataSync::Agent.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-datasync.git",
  "definitions" : {
    "Tag" : {
      "additionalProperties" : False,
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key for an AWS resource tag.",
          "pattern" : "^[a-zA-Z0-9\\s+=._:/-]+$",
          "maxLength" : 256,
          "minLength" : 1
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for an AWS resource tag.",
          "pattern" : "^[a-zA-Z0-9\\s+=._:@/-]+$",
          "maxLength" : 256,
          "minLength" : 1
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "AgentName" : {
      "description" : "The name configured for the agent. Text reference used to identify the agent in the console.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9\\s+=._:@/-]+$",
      "maxLength" : 256,
      "minLength" : 0
    },
    "ActivationKey" : {
      "description" : "Activation key of the Agent.",
      "type" : "string",
      "pattern" : "[A-Z0-9]{5}(-[A-Z0-9]{5}){4}",
      "maxLength" : 29
    },
    "SecurityGroupArns" : {
      "description" : "The ARNs of the security group used to protect your data transfer task subnets.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "pattern" : "^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\\-0-9]*:[0-9]{12}:security-group/.*$",
        "maxLength" : 128
      }
    },
    "SubnetArns" : {
      "description" : "The ARNs of the subnets in which DataSync will create elastic network interfaces for each data transfer task.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "pattern" : "^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\\-0-9]*:[0-9]{12}:subnet/.*$",
        "maxLength" : 128
      }
    },
    "VpcEndpointId" : {
      "description" : "The ID of the VPC endpoint that the agent has access to.",
      "type" : "string",
      "pattern" : "^vpce-[0-9a-f]{17}$"
    },
    "EndpointType" : {
      "description" : "The service endpoints that the agent will connect to.",
      "type" : "string",
      "enum" : [ "FIPS", "PUBLIC", "PRIVATE_LINK" ]
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "AgentArn" : {
      "description" : "The DataSync Agent ARN.",
      "type" : "string",
      "pattern" : "^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$",
      "maxLength" : 128
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "datasync:TagResource", "datasync:UntagResource", "datasync:ListTagsForResource" ]
  },
  "additionalProperties" : False,
  "required" : [ ],
  "readOnlyProperties" : [ "/properties/AgentArn", "/properties/EndpointType" ],
  "primaryIdentifier" : [ "/properties/AgentArn" ],
  "createOnlyProperties" : [ "/properties/ActivationKey", "/properties/SecurityGroupArns", "/properties/SubnetArns", "/properties/VpcEndpointId" ],
  "writeOnlyProperties" : [ "/properties/ActivationKey" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "datasync:CreateAgent", "datasync:TagResource", "datasync:DescribeAgent", "datasync:ListTagsForResource", "ec2:DescribeNetworkInterfaces", "ec2:DescribeSecurityGroups", "ec2:DescribeSubnets", "ec2:DescribeVpcEndpoints" ]
    },
    "read" : {
      "permissions" : [ "datasync:DescribeAgent", "datasync:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "datasync:UpdateAgent", "datasync:DescribeAgent", "datasync:ListTagsForResource", "datasync:TagResource", "datasync:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "datasync:DeleteAgent" ]
    },
    "list" : {
      "permissions" : [ "datasync:ListAgents" ]
    }
  }
}