SCHEMA = {
  "typeName" : "AWS::SecurityHub::ProductSubscription",
  "description" : "The AWS::SecurityHub::ProductSubscription resource represents a subscription to a service that is allowed to generate findings for your Security Hub account. One product subscription resource is created for each product enabled.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-securityhub",
  "properties" : {
    "ProductArn" : {
      "description" : "The generic ARN of the product being subscribed to",
      "type" : "string",
      "pattern" : "arn:aws\\S*:securityhub:\\S*"
    },
    "ProductSubscriptionArn" : {
      "description" : "The ARN of the product subscription for the account",
      "type" : "string",
      "pattern" : "arn:aws\\S*:securityhub:\\S*"
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/ProductSubscriptionArn" ],
  "required" : [ "ProductArn" ],
  "createOnlyProperties" : [ "/properties/ProductArn" ],
  "readOnlyProperties" : [ "/properties/ProductSubscriptionArn" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "securityhub:EnableImportFindingsForProduct" ]
    },
    "read" : {
      "permissions" : [ "securityhub:ListEnabledProductsForImport" ]
    },
    "delete" : {
      "permissions" : [ "securityhub:ListEnabledProductsForImport", "securityhub:DisableImportFindingsForProduct" ]
    },
    "list" : {
      "permissions" : [ "securityhub:ListEnabledProductsForImport" ]
    }
  }
}