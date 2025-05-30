SCHEMA = {
  "typeName" : "AWS::Shield::ProtectionGroup",
  "description" : "A grouping of protected resources so they can be handled as a collective. This resource grouping improves the accuracy of detection and reduces False positives.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-shield.git",
  "primaryIdentifier" : [ "/properties/ProtectionGroupArn" ],
  "readOnlyProperties" : [ "/properties/ProtectionGroupArn" ],
  "createOnlyProperties" : [ "/properties/ProtectionGroupId" ],
  "replacementStrategy" : "delete_then_create",
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "tagProperty" : "/properties/Tags",
    "cloudFormationSystemTags" : False,
    "permissions" : [ "shield:ListTagsForResource", "shield:UntagResource", "shield:TagResource" ]
  },
  "additionalProperties" : False,
  "required" : [ "Aggregation", "Pattern", "ProtectionGroupId" ],
  "properties" : {
    "ProtectionGroupId" : {
      "description" : "The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it.",
      "type" : "string",
      "pattern" : "[a-zA-Z0-9\\-]*",
      "minLength" : 1,
      "maxLength" : 36
    },
    "ProtectionGroupArn" : {
      "description" : "The ARN (Amazon Resource Name) of the protection group.",
      "type" : "string"
    },
    "Aggregation" : {
      "description" : "Defines how AWS Shield combines resource data for the group in order to detect, mitigate, and report events.\n* Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.\n* Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.\n* Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront and origin resources for CloudFront distributions.",
      "type" : "string",
      "enum" : [ "SUM", "MEAN", "MAX" ]
    },
    "Pattern" : {
      "description" : "The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource Amazon Resource Names (ARNs), or include all resources of a specified resource type.",
      "type" : "string",
      "enum" : [ "ALL", "ARBITRARY", "BY_RESOURCE_TYPE" ]
    },
    "Members" : {
      "description" : "The Amazon Resource Names (ARNs) of the resources to include in the protection group. You must set this when you set `Pattern` to `ARBITRARY` and you must not set it for any other `Pattern` setting.",
      "type" : "array",
      "insertionOrder" : False,
      "maxItems" : 10000,
      "items" : {
        "type" : "string",
        "minLength" : 1,
        "maxLength" : 2048
      }
    },
    "ResourceType" : {
      "description" : "The resource type to include in the protection group. All protected resources of this type are included in the protection group. Newly protected resources of this type are automatically added to the group. You must set this when you set `Pattern` to `BY_RESOURCE_TYPE` and you must not set it for any other `Pattern` setting.",
      "type" : "string",
      "enum" : [ "CLOUDFRONT_DISTRIBUTION", "ROUTE_53_HOSTED_ZONE", "ELASTIC_IP_ALLOCATION", "CLASSIC_LOAD_BALANCER", "APPLICATION_LOAD_BALANCER", "GLOBAL_ACCELERATOR" ]
    },
    "Tags" : {
      "description" : "One or more tag key-value pairs for the Protection object.",
      "type" : "array",
      "insertionOrder" : False,
      "maxItems" : 200,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "definitions" : {
    "Tag" : {
      "description" : "A tag associated with an AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing or other management. Typically, the tag key represents a category, such as \"environment\", and the tag value represents a specific value within that category, such as \"test,\" \"development,\" or \"production\". Or you might set the tag key to \"customer\" and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "required" : [ "Key", "Value" ],
      "properties" : {
        "Key" : {
          "description" : "Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as \"customer.\" Tag keys are case-sensitive.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "description" : "Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as \"companyA\" or \"companyB.\" Tag values are case-sensitive.",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      }
    }
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "shield:CreateProtectionGroup", "shield:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "shield:DeleteProtectionGroup", "shield:UntagResource" ]
    },
    "read" : {
      "permissions" : [ "shield:DescribeProtectionGroup", "shield:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "shield:UpdateProtectionGroup", "shield:ListTagsForResource", "shield:TagResource", "shield:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "shield:ListProtectionGroups" ]
    }
  }
}