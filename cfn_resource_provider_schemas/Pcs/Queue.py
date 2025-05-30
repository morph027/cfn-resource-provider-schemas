SCHEMA = {
  "typeName" : "AWS::PCS::Queue",
  "description" : "AWS::PCS::Queue resource creates an AWS PCS queue.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-pcs.git",
  "definitions" : {
    "ComputeNodeGroupConfiguration" : {
      "type" : "object",
      "description" : "The compute node group configuration for a queue.",
      "properties" : {
        "ComputeNodeGroupId" : {
          "type" : "string",
          "description" : "The compute node group ID for the compute node group configuration."
        }
      },
      "additionalProperties" : False
    },
    "ErrorInfo" : {
      "type" : "object",
      "description" : "An error that occurred during resource provisioning.",
      "properties" : {
        "Code" : {
          "type" : "string",
          "description" : "The short-form error code."
        },
        "Message" : {
          "type" : "string",
          "description" : "The detailed error information."
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "description" : "The unique Amazon Resource Name (ARN) of the queue.",
      "pattern" : "^(.*?)"
    },
    "ClusterId" : {
      "type" : "string",
      "description" : "The ID of the cluster of the queue."
    },
    "ComputeNodeGroupConfigurations" : {
      "type" : "array",
      "description" : "The list of compute node group configurations associated with the queue. Queues assign jobs to associated compute node groups.",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/ComputeNodeGroupConfiguration"
      }
    },
    "ErrorInfo" : {
      "type" : "array",
      "description" : "The list of errors that occurred during queue provisioning.",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/ErrorInfo"
      }
    },
    "Id" : {
      "type" : "string",
      "description" : "The generated unique ID of the queue."
    },
    "Name" : {
      "type" : "string",
      "description" : "The name that identifies the queue."
    },
    "Status" : {
      "type" : "string",
      "description" : "The provisioning status of the queue. The provisioning status doesn't indicate the overall health of the queue.",
      "enum" : [ "CREATING", "ACTIVE", "UPDATING", "DELETING", "CREATE_FAILED", "DELETE_FAILED", "UPDATE_FAILED" ]
    },
    "Tags" : {
      "type" : "object",
      "description" : "1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.",
      "patternProperties" : {
        "^.+$" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "required" : [ "ClusterId" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/ClusterId" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/ErrorInfo", "/properties/Id", "/properties/Status" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateNetworkInterface", "ec2:DescribeVpcs", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups", "ec2:GetSecurityGroupsForVpc", "iam:CreateServiceLinkedRole", "secretsmanager:CreateSecret", "secretsmanager:TagResource", "pcs:CreateQueue", "pcs:GetQueue", "pcs:ListTagsForResource", "pcs:TagResource" ],
      "timeoutInMinutes" : 60
    },
    "read" : {
      "permissions" : [ "pcs:GetQueue", "pcs:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "pcs:GetQueue", "pcs:UpdateQueue", "pcs:ListTagsForResource", "pcs:TagResource", "pcs:UntagResource" ],
      "timeoutInMinutes" : 60
    },
    "delete" : {
      "permissions" : [ "pcs:DeleteQueue", "pcs:GetQueue" ],
      "timeoutInMinutes" : 60
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "ClusterId" : {
            "$ref" : "resource-schema.json#/properties/ClusterId"
          }
        },
        "required" : [ "ClusterId" ]
      },
      "permissions" : [ "pcs:ListClusters", "pcs:ListQueues" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "pcs:TagResource", "pcs:ListTagsForResource", "pcs:UntagResource" ]
  }
}